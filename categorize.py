#!/usr/bin/env python
import re
import sys
from collections import defaultdict

import yaml


_split_pat = re.compile(r'\s*(?<!\\)\*\s*')

def parse_ingredients(ingredient_str, pat=_split_pat):
    return (pat.split(ingredient_str) + [None])[:2]


def format_with_recipe(item, amt, recipe):
    return [1 if amt is None else amt, recipe]


def format_amount(item, amt, recipe):
    return 'some' if amt is None else amt


def make_list(recipes, fmtf=format_amount):
    dd = defaultdict(list)
    for k, vs in recipes.items():
        for v in vs:
            item, amt = parse_ingredients(v)
            dd[item].append(fmtf(item, amt, k))
    return dd


def main():
    recipes = yaml.load(sys.stdin)
    ingredients = make_list(recipes)
    print(yaml.dump(ingredients))


if __name__ == '__main__':
    main()
