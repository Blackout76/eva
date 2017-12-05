"""
evepaste.parsers.industry
~~~~~~~~~~~~~~~~~~~~~~~~~
Parse listings for the industry interface.

"""
from collections import defaultdict
import re

from evepaste.utils import regex_match_lines, f_int


# Medium Mercoxit Mining Crystal Optimization I Blueprint  8   0   -1  Rig Resource Processing
INDUSTRY_RE = re.compile(r"""^([\S ]*)                         # name
                            \t([\d,'\.]*)                      # material efficiency
                            \t([\d,'\.]*)                      # time efficiency
                            \t([\d,'\.]*)                      # runs
                            (\t([\S ]*))                       # group
                           """, re.X)



def parse_industry(lines):
    """ Parse Industry

    :param string paste_string: A raw string pasted from the industry
    """
    matches, bad_lines = regex_match_lines(INDUSTRY_RE, lines)

    items = defaultdict(int)

    for name, count in matches:
        items[name.strip()] += f_int(count)

    results = []
    for name, me, te, runs, group in sorted(items.items()):
        item = {'name': name,
                'me': me,
                'te': te,
                'runs': runs,
                'group': group,}

        results.append(item)

    return results, bad_lines
