#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from browseragents import core


class BrowserTestCase(unittest.TestCase):

    def test_firefox(self):
        f = core.random(browser="firefox")
        self.assertTrue("Firefox" in f)

    def test_chrome(self):
        c = core.random(browser="chrome")
        self.assertTrue("Chrome" in c)
