# A part of pdfrw (https://github.com/pmaupin/pdfrw)
# Copyright (C) 2006-2015 Patrick Maupin, Austin, Texas
# MIT license -- See LICENSE.txt for details
"""
PDF file reader/writer library
"""

from .pdfwriter import PdfWriter
from .pdfreader import PdfReader
from .objects import (PdfObject, PdfName, PdfArray,
                      PdfDict, IndirectPdfDict, PdfString)
from .tokens import PdfTokens
from .errors import PdfParseError
from .pagemerge import PageMerge
from ._version import __version__

# Add a tiny bit of compatibility to pyPdf

PdfFileReader = PdfReader
PdfFileWriter = PdfWriter

__all__ = """PdfWriter PdfReader PdfObject PdfName PdfArray
             PdfTokens PdfParseError PdfDict IndirectPdfDict
             PdfString PageMerge __version__""".split()

