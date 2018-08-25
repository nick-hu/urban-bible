#!/usr/bin/env python

import csv
import random
import re
import sys

from os import path

import transformations as tf


def translate(text):
    for row in subs:
        word = row[0]
        text = re.sub(r"\b{}\b".format(word), lambda _: random.choice(row[1:]),
                      text, flags=re.MULTILINE)

    text = tf.very_af(text)

    return text


subs = []

for i in range(1, len(sys.argv) - 1):
    with open(sys.argv[i]) as subfile:
        for row in csv.reader(subfile):
            sub = list(filter(None, row))
            if len(sub) > 1:
                subs.append(sub)

name, ext = path.splitext(path.realpath(sys.argv[-1]))
outfile_name = "{}_new{}".format(name, ext)

text = open(sys.argv[-1]).read()

with open(outfile_name, 'w') as outfile:
    outfile.write(translate(text))
