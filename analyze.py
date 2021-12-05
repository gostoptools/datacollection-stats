#!/usr/bin/env python3

import argparse
import os
from os import path
from importlib import import_module

parser = argparse.ArgumentParser(description='Run analysis tests')

parser.add_argument('tests', nargs="*", help="tests to carry out (python files from scripts directory)")
parser.add_argument('--all', '-a', help="carry out all tests", action='store_true')

args = parser.parse_args();

files = args.tests

if args.all:
    pythonfiles = filter(lambda s: len(s) >= 3 and s[-3:] == ".py",
            os.listdir(path.dirname(__file__) + "/scripts"))
    files = list(map(lambda x : x[:-3], pythonfiles))


for f in files:
    test = path.join(path.dirname(__file__), "scripts", f + ".py")
    if not path.exists(path.join(path.dirname(__file__), "scripts", f + ".py")):
        raise FileNotFoundError(test)

for f in files:
    print("="* 10)
    print(f"Testing '{f}':")
    print()
    import_module(f"scripts.{f}")
    print()
