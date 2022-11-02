# A part of pdfrw (https://github.com/pmaupin/pdfrw)
# Copyright (C) 2006-2015 Patrick Maupin, Austin, Texas
# MIT license -- See LICENSE.txt for details
"""
PDF file reader/writer library
"""

from ._version import __version__
from .errors import PdfParseError
from .objects import (
    IndirectPdfDict,
    PdfArray,
    PdfDict,
    PdfName,
    PdfObject,
    PdfString,
)
from .pagemerge import PageMerge
from .pdfreader import PdfReader
from .pdfwriter import PdfWriter
from .tokens import PdfTokens

# Add a tiny bit of compatibility to pyPdf

PdfFileReader = PdfReader
PdfFileWriter = PdfWriter

__all__ = """PdfWriter PdfReader PdfObject PdfName PdfArray
             PdfTokens PdfParseError PdfDict IndirectPdfDict
             PdfString PageMerge __version__""".split()

