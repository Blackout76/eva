"""
evepaste.parsers.assets
~~~~~~~~~~~~~~~~~~~~~~~
Parse eve online asset lists. This also invludes inventory listings.

"""
import re

from evepaste.utils import regex_match_lines, f_int

ASSET_LIST_RE = re.compile(r"""^([\S ]*)                           # name
                                \t([\d,'\.]*)                      # quantity
                                (\t([\S ]*))?                      # group
                                (\t(XLarge|Large|Medium|Small|))?  # size
                                (\t([\d ,\.]* m3))?                # volume
                                (\t(High|Medium|Low|Rigs|[\d ]*))? # slot
                               """, re.X)


def parse_assets(lines):
    """ Parse asset list

    :param string paste_string: An asset list string
    """
    matches, bad_lines = regex_match_lines(ASSET_LIST_RE, lines)

    result = [{'name': name,
               'quantity': f_int(quantity) or 1,
               'group': group,
               'size': size,
               'volume': volume,
               'slot': slot,}
              for (name,
                   quantity,
                   _, group,
                   _, size,
                   _, volume,
                   _, slot) in matches]
    return result, bad_lines
