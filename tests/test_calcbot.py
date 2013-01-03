# coding=utf-8
from errbot.backends.test import FullStackTest

class TestCommands(FullStackTest):
    @classmethod
    def setUpClass(cls, extra=None):
        super().setUpClass(__file__)

    def test_calc(self):
        self.assertCommand('!calc 2x²-x-1=0', 'x = 1 or x = -0.5')
