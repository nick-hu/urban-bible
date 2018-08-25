#!/usr/bin/env python

import re

from nltk import pos_tag


def very_af(text):

    def repl(match):
        word = match.group(1)
        pos = pos_tag(["very", word])[1][1]

        if pos == "JJ":  # word is adjective
            return word + " af"

        return "very " + word

    return re.sub(r"(?<!\ba\b\s)\bvery\s*\b(\w*)\b", repl,
                  text, flags=re.MULTILINE)
