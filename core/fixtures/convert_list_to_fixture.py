import argparse
from collections import defaultdict

import simplejson


def list_to_facet_fixture(facet_type, items):
    out = []

    items = items.split('\n')

    for v in items:
        d = defaultdict()
        d['model'] = 'core.facet'
        d['fields'] = defaultdict()
        d['fields']['facet_type'] = facet_type
        d['fields']['title'] = v.lower()
        out.append(d)

    return simplejson.dumps(out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'facet_type', help='the facet type')
    parser.add_argument(
        'items', help='a string with a list of items separated by a new line')
    args = parser.parse_args()

    print(list_to_facet_fixture(args.facet_type, args.items))
