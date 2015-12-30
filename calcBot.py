# -*- coding: utf-8 -*-
from errbot import botcmd, BotPlugin

import subprocess
import os

QALC_PATH = os.environ.get('QALC_PATH', '/usr/bin/qalc')


class CalcBot(BotPlugin):

    @botcmd
    def calc(self, mess, args):
        """ Calculate, solve or convert the given expression.
        Examples: !calc 5+2
        !calc x²+x+1=5
        !calc 5 in² = x cm²
        """
        if not os.path.exists(QALC_PATH):
            return ('ERROR: this plugin requires libqalculate with the qalc command o be installed. '
                    'On gentoo it requires the readline useflag. To customize `qalq` path, set the '
                    'environment variable QALC_PATH (default to /usr/bin/qalc)'
        if not args:
            return 'Please give me an expression to solve'
        p = subprocess.Popen([QALC_PATH, '-t', args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return p.stdout.read().decode().strip()
