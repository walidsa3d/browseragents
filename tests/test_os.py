#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from browseragents import core


class OSTestCase(unittest.TestCase):

    def test_windows(self):
        f = core.random(os="windows")
        self.assertTrue("Windows" in f)

    def test_linux(self):
        c = core.random(os="linux")
        self.assertTrue("Linux" in c)
