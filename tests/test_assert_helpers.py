#! /usr/bin/env python
# A part of forked pdfrw
# Copyright (C) 2022 Stephen Arnold <nerdboy@gentoo.org>
# MIT license -- See LICENSE.txt for details

'''
Run from the directory above like so:
python -m tests.test_assert_helpers
'''

import unittest

from pdfrw.errors import (
    assert_eq,
    assert_none,
    assert_not,
    assert_notin,
    assert_notnone,
    assert_range,
)

import pytest


class TestAsserts(unittest.TestCase):
    str_var = 'fubar'
    int_var = 42
    none_var = None

    def test_assert_eq(self):
        self.assertEqual(self.str_var, 'fubar')
        assert_eq(self.str_var, 'fubar')

    def test_assert_eq_raises(self):
        some_string = 'ouch'
        with pytest.raises(AssertionError):
            assert_eq(self.str_var, some_string)

    def test_assert_none(self):
        assert_none(self.none_var)

    def test_assert_none_raises(self):
        some_string = 'ouch'
        with pytest.raises(AssertionError):
            assert_none(some_string)

    def test_assert_not(self):
        assert_not(self.none_var)

    def test_assert_not_raises(self):
        some_string = 'ouch'
        with pytest.raises(AssertionError):
            assert_not(some_string)

    def test_assert_notin(self):
        assert_notin('baz', self.str_var)

    def test_assert_notin_raises(self):
        some_string = 'ouch'
        with pytest.raises(AssertionError):
            assert_notin('ch', some_string)

    def test_assert_notnone(self):
        assert_notnone(self.int_var)

    def test_assert_notnone_raises(self):
        with pytest.raises(AssertionError):
            assert_notnone(self.none_var)

    def test_assert_range(self):
        assert_range(self.int_var, 1, 50)

    def test_assert_range_raises(self):
        with pytest.raises(AssertionError):
            assert_range(self.int_var, 1, 25)


if __name__ == '__main__':
    unittest.main()
