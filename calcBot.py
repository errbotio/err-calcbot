# -*- coding: utf-8 -*-

from botplugin import BotPlugin
from jabberbot import botcmd
import subprocess
CMD = '/usr/bin/qalc'
class CalcBot(BotPlugin):

    @botcmd
    def calc(self, mess, args):
        """ Calculate, solve or convert the given expression.
        Examples: !calc 5+2
        !calc x²+x+1=5
        !calc 5 in² = x cm²
        """
        if not os.path.exists(CMD):
            return 'ERROR: this plugin requires libqalculate with the qalc command to be installed. On gentoo it requires the readline useflag.'
        if not args:
            return 'Please give me an expression to solve'
        p = subprocess.Popen(['/usr/bin/qalc', '-t', args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return p.stdout.read()
