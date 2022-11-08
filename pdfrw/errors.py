# A part of pdfrw (https://github.com/pmaupin/pdfrw)
# Copyright (C) 2006-2015 Patrick Maupin, Austin, Texas
# MIT license -- See LICENSE.txt for details

'''
PDF Exceptions and error handling
'''

import logging

fmt = logging.Formatter('[%(levelname)s] %(filename)s:%(lineno)d %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(fmt)

log = logging.getLogger('pdfrw')
log.setLevel(logging.WARNING)
log.addHandler(handler)


class PdfError(Exception):
    "Abstract base class of exceptions thrown by this module"

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class PdfParseError(PdfError):
    "Error thrown by parser/tokenizer"


class PdfOutputError(PdfError):
    "Error thrown by PDF writer"


class PdfNotImplementedError(PdfError):
    "Error thrown on missing features"


def assert_eq(something, otherthing):
    """
    Assertion equality helper to replace legacy code.
    """
    if not something == otherthing:
        raise AssertionError(f'Assert {something} eq {otherthing} failed')


def assert_none(something):
    """
    Assertion none helper to replace legacy code.
    """
    if something is None:
        return
    raise AssertionError(f'Assert {something} is None failed')


def assert_not(something):
    """
    Assertion not helper to replace legacy code.
    """
    if not something:
        return
    raise AssertionError(f'Assert not {something} failed')


def assert_notin(something, otherthing):
    """
    Assertion not in helper to replace legacy code.
    """
    if something not in otherthing:
        return
    raise AssertionError(f'Assert {something} not in {otherthing} failed')


def assert_notnone(something):
    """
    Assertion none helper to replace legacy code.
    """
    if something is not None:
        return
    raise AssertionError(f'Assert {something} is not None failed')


def assert_range(something, lower=1, upper=16):
    """
    Assertion in range helper to replace legacy code.
    """
    if lower <= something <= upper:
        return
    raise AssertionError(f'Assert {something} in range {lower} - {upper} failed')
