# -*- coding: utf-8 -*-
import base64
import zlib
import re, collections

def words(text): return re.findall('[a-z]+', text.lower()) 
    
def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS_BIG = train(words(file('corpus.txt').read()))
NWORDS = {}
for key in NWORDS_BIG:
    if NWORDS_BIG[key] >= 8:
        NWORDS[key] = NWORDS_BIG[key]

serialized = base64.encodestring(zlib.compress(str(NWORDS), 9))

with open("serialized.txt", "w") as f_out:
        f_out.write(serialized)