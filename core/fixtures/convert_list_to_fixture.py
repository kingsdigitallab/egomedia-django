import argparse
from collections import defaultdict

import simplejson


def list_to_facet_fixture(items, model):
    out = []

    items = items.split('\n')

    for k, v in enumerate(items):
        d = defaultdict()
        d['model'] = model
        d['pk'] = k + 1
        d['fields'] = defaultdict()
        d['fields']['title'] = v.lower()
        out.append(d)

    return simplejson.dumps(out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'items', help='a string with a list of items separated by a new line')
    parser.add_argument(
        'model', help='model name, app.modelname, to create the fixture for')
    args = parser.parse_args()

    print(list_to_facet_fixture(args.items, args.model))
