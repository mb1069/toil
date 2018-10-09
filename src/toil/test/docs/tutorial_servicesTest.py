from __future__ import absolute_import
import unittest
import os
import sys

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # noqa
sys.path.insert(0, pkg_root)  # noqa

from toil import subprocess
from toil.test import ToilTest

class ToilWdlIntegrationTest(ToilTest):
    # a test for tutorial_services.py

    def setUp(self):
        self.program = os.path.abspath("scripts/tutorial_services.py")

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testExitCode(self):
        out = subprocess.call(["python", self.program, "file:my-jobstore", "--clean=always"])
        assert out == 0, out

if __name__ == "__main__":
    unittest.main()  # run all tests


