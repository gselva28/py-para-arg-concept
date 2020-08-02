# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:09:06 2020

@author: SELVAKUMAR
"""

def strproc(*args):
    ans = ([x.upper() for x in args])
    return sorted(ans)

print(strproc("guava","apple","orange","grapes"))
