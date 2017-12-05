from collections import defaultdict
import json
import evepaste
from evepaste import parsers
from evepaste.parsers import industry
from .helpers import iter_types
from re import sub

TYPES = json.loads(open('data/types.json').read())
TYPES_BY_NAME = dict((t['typeName'].lower(), t) for t in TYPES)
TYPES_BY_ID = dict((t['typeID'], t) for t in TYPES)

def parse(content):
	parser_list = list(evepaste.PARSER_TABLE) + [
		('listing', listing_parser),
		('heuristic', tryhard_parser),
		('industry', industry.parse_industry),
	]

	results = []

	try:
		kind, result, bad_lines = evepaste.parse(content, parsers=parser_list)
		if result:
			for item in iter_types(kind, result):
				details = get_type_by_name(item['name'])
				if details:
					item['typeID'] = details['typeID']
					item['groupID'] = details['groupID']
					item['market'] = details['market']
					results.append(item)
	except evepaste.Unparsable:
		raise

	return {'representative_kind': kind,
			'results': results,
			'bad_lines': bad_lines}

def listing_parser(lines):
	results = defaultdict(int)
	bad_lines = []
	lines = [line.strip() for line in lines]
	for line in lines:
		if get_type_by_name(line):
			results[line] += 1
		else:
			result, bad_line = parsers.parse_listing([line])
			for r in result:
				if get_type_by_name(r['name']):
					results[r['name']] += r.get('quantity', 1)
				else:
					bad_lines.append(line)
			for l in bad_line:
				bad_lines.append(l)

	return [{'name': name, 'quantity': quantity} for name, quantity in results.items()], bad_lines

def tryhard_parser(lines):
	results = defaultdict(int)
	bad_lines = []

	for line in lines:
		parts = [part.strip(', ') for part in line.split('\t')]
		if len(parts) == 1:
			parts = [part.strip(',\t ') for part in line.split('  ')]
			parts = [part for part in parts if part]

		if len(parts) == 1:
			parts = [part.strip(',') for part in line.split(' ')]
			parts = [part for part in parts if part]

		# This should only work for multi-part lines
		if len(parts) == 1:
			break

		combinations = [['name', 'quantity'],
						[None, 'name', None, 'quantity'],
						['quantity', None, 'name'],
						['quantity', 'name'],
						[None, 'name'],
						['name']]
		for combo in combinations:
			if len(combo) > len(parts):
				continue

			name = ''
			quantity = 1
			for i, part in enumerate(combo):
				if part == 'name':
					if get_type_by_name(parts[i]):
						name = parts[i]
					else:
						break
				elif part == 'quantity':
					if int_convert(parts[i]):
						quantity = int_convert(parts[i])
					else:
						break
			else:
				results[name] += quantity
				break
		else:
			# The above method failed. Now let's try splitting on spaces and
			# build each part until we find a valid type
			parts = [part.strip(',\t ') for part in line.split(' ')]
			for i in range(len(parts)):
				name = ' '.join(parts[:-i])
				if name and get_type_by_name(name):
					results[name] += 1
					break
			else:
				bad_lines.append(line)

	if not results:
		raise evepaste.Unparsable('No valid input')

	return [{'name': name, 'quantity': quantity} for name, quantity in results.items()], bad_lines

def int_convert(s):
	try:
		return int(sub(r"[,'\. 'x]", '', s))
	except ValueError:
		return


def get_type_by_name(name):
	if not name:
		return
	s = name.lower().strip()
	return (TYPES_BY_NAME.get(s.rstrip('*')) or TYPES_BY_NAME.get(s))


def get_type_by_id(typeID):
	if not typeID:
		return
	return TYPES_BY_ID.get(typeID)