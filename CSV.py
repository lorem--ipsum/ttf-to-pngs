#!/usr/bin/env python

import re

def load(path, converter):
    if not converter or not hasattr(converter, '__call__'):
        raise InputError('converter must be callable')
    
    result = []
    
    with open(path) as f:
        for line in f:
            result.append(converter(re.match(r'(.*),\s(.*)', line).groups()))
            
    return result