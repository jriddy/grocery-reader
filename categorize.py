#!/usr/bin/env python
import re
import sys
from collections import defaultdict

import yaml


_split_pat = re.compile(r'\s+\*\s+')

def parse_ingredients(ingredient_str, pat=_split_pat):
    return (pat.split(ingredient_str) + [None])[:2]


def make_list(recipes):
    dd = defaultdict(list)
    for k, vs in recipes.items():
        for v in vs:
            item, amt = parse_ingredients(v)
            dd[item].append(amt)
    return dd


def main():
    recipes = yaml.load(sys.stdin)
    ingredients = make_list(recipes)
    print(yaml.dump(ingredients))


if __name__ == '__main__':
    main()
