#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple script to help test the program
Copyright 2019 <jimmy-zx>
Feature:
    Automatically scan the test folder
    Output the correctness
    Prompt wrong output
How to use:
    1. Put your program into this folder (Assume the name is {target}.{exe|o})
    2. Put your test data ({name}.in and {name}.ans) into the {target} folder
    3. Run this script
Demo file structure:
    +Project folder
    |+test_app      Test data folder
    ||test1.in      Test data
    ||test1.ans
    ||test2.in
    ||test2.ans
    ||...
    |test_app.o     Test target
    |test.py        This application
Warning:
    If the file of folder does not exist, the program might not behave as defined
    This program has been tested on Ubuntu 18.04,
        however, behavior on other platforms are not yet tested
"""

import os
import subprocess

# Initialize data
if os.name == 'nt':
    EXEC_EXT = '.exe'
else:
    EXEC_EXT = '.o'

TARGET = "happy"
EXEC_NAME = os.path.join('.', TARGET + EXEC_EXT)
DATA_DIR = os.path.join('.', TARGET)
DATA_FILES = list()

# Fetch data files
for root, dirs, files in os.walk(os.path.join(DATA_DIR)):
    for name in files:
        if name[-3:] == '.in':
            DATA_FILES.append(os.path.join(DATA_DIR, name))

SCORE = 0

# Test
for data_file in DATA_FILES:
    p = subprocess.Popen([EXEC_NAME],
                         stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    with open(data_file) as f:
        res = p.communicate(f.read().encode())
    with open(data_file.replace('.in', '.ans')) as f:
        output = res[0].decode()
        excepted = f.read()
        if output == excepted:
            SCORE += 1
        else:
            print("Test not passed for input file {}".format(data_file))
            print("Excepted output: {}".format(excepted))
            print("Real output: {}".format(output))

# Output
print("{}/{}({}%) data(s) passed".format(
    SCORE, len(DATA_FILES), SCORE / len(DATA_FILES) * 100))
