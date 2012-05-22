from botplugin import BotPlugin
from jabberbot import botcmd
import subprocess

class CalcBot(BotPlugin):

    @botcmd
    def calc(self, mess, args):
        """ Calculate, solve or convert the given expression.
        Examples: !calc 5+2
        !calc x²+x+1=5
        !calc 5 in² = x cm²
        """
        if not args:
            return 'Please give me an expression to solve'
        p = subprocess.Popen(['/usr/bin/qalc', '-t', args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return p.stdout.read()
