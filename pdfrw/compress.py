# A part of pdfrw (https://github.com/pmaupin/pdfrw)
# Copyright (C) 2006-2015 Patrick Maupin, Austin, Texas
# MIT license -- See LICENSE.txt for details

'''
Currently, this sad little file only knows how to compress
using the flate (zlib) algorithm.  Maybe more later, but it's
not a priority for me...
'''

from .objects.pdfname import default_pdfname
from .py23_diffs import convert_load, convert_store, zlib
from .uncompress import streamobjects


def compress(mylist):
    flate = default_pdfname.FlateDecode
    for obj in streamobjects(mylist):
        ftype = obj.Filter
        if ftype is not None:
            continue
        oldstr = obj.stream
        newstr = convert_load(zlib.compress(convert_store(oldstr)))
        if len(newstr) < len(oldstr) + 30:
            obj.stream = newstr
            obj.Filter = flate
            obj.DecodeParms = None
