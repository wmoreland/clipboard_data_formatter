#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
When run, takes data from clipboard and reformats it to be enclosed by brackets
and separated by a comma and space. It then copies the output back to the
clipboard.

Useful for taking data from sources such as https://apps.automeris.io/wpd/ and
pasting it into Python scripts as a tuple to plot it.

Note the decimal separator must be a period.
"""

import pandas
import io
import pyperclip
import csv

try:
    df = pandas.read_clipboard(header=None, sep=',|\t|;|\s', engine='python')

    try:
        df[0] = '[' + df[0].map(str) + ', ' + df[1].map(str) + '],'
        outbuf = io.StringIO()
    
        df.to_csv(outbuf, columns=[0], header=False, index=False,
                  sep='|', quoting=csv.QUOTE_NONE)
#        df.to_csv('test_output.csv', columns=[0], header=False, index=False,
#                  sep='|', quoting=csv.QUOTE_NONE)
        
        pyperclip.copy(outbuf.getvalue())
#        print(pyperclip.paste())
        
    except KeyError:
        print('KeyError: Clipboard does not contain two columns of data')

except pandas.errors.ParserError:
    print('ParserError: Pandas was unable to parse the clipboard')
