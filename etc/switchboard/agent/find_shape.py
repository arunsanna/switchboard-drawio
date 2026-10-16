#!/usr/bin/env python3
"""Searches draw.io's shape library (10,000+ shapes, JGraph's drawio-mcp search index) by words.

Prints the best matches as JSON lines: title, default width and height, and the style string to
copy into the diagram exactly. A word matches a whole word or the start of one; words in the
title count most, and current AWS shapes (mxgraph.aws4) rank above the old ones.

Usage: python3 find_shape.py internet gateway
"""
import json
import os
import re
import sys

words = [word for argument in sys.argv[1:] for word in argument.lower().split()]
if not words:
    sys.exit(__doc__)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "search-index.json")) as file:
    index = json.load(file)


def tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def match(word, found):
    if word in found:
        return 2
    return 1 if any(token.startswith(word) for token in found) else 0


def score(item):
    title = tokens(item.get("title", ""))
    every = title + tokens(item.get("tags", ""))
    points = 0
    for word in words:
        hit = match(word, every)
        if hit == 0:
            return 0
        points += hit + (2 if match(word, title) else 0)
    style = item.get("style", "")
    if "mxgraph.aws4" in style:
        points += 3
    elif "mxgraph.aws3" in style or "mxgraph.aws2" in style:
        points -= 3
    return points


hits = sorted((item for item in index if score(item) > 0), key=score, reverse=True)[:8]
for hit in hits:
    print(json.dumps({"title": hit.get("title"), "w": hit.get("w"), "h": hit.get("h"), "style": hit.get("style")}))
if not hits:
    print("no match; try fewer or other words")
