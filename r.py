#!/usr/bin/env python
import re
m = re.search('\\[rtfvn]', r'Hello World!\n')
if m is not None:
    m.group()


m = re.search(r'\\[rtfvn]', r'Hello World!\n')
if m is not None:
    m.group
