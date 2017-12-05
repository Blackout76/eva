def iter_types(kind, result):
	if kind == 'bill_of_materials':
		for item in result:
			yield {'name': item['name'],
				   'quantity': item.get('you', item.get('quantity'))}
	elif kind == 'eft':
		yield {'name': result['ship'], 'quantity': 1}
		for item in result['modules']:
			yield item
			if item.get('ammo'):
				yield {'name': item['ammo'], 'quantity': 1}
	elif kind == 'killmail':
		yield {'name': result['victim']['destroyed'],
			   'quantity': 1,
			   'destroyed': True}
		for item in result['dropped']:
			item['dropped'] = True
			yield item
		for item in result['destroyed']:
			item['destroyed'] = True
			yield item
	elif kind == 'wallet':
		for item in result:
			if item.get('name'):
				yield item
	elif kind == 'chat':
		for item in result['items']:
			item['quantity'] = item.get('quantity', 1)
			yield item
	else:
		for item in result:
			item['quantity'] = item.get('quantity', 1)
			yield item