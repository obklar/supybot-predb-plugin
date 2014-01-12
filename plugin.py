import pre

import supybot.log as log
import supybot.conf as conf
import supybot.utils as utils
import supybot.world as world
import supybot.ircdb as ircdb
from supybot.commands import *
import supybot.irclib as irclib
import supybot.ircmsgs as ircmsgs
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


class Dupe(callbacks.Plugin):

    def _dupe(self, irc, query, limit):
        results = pre.dupe(query, limit)
        if (results):
            irc.reply(format('Got %s.', results))
        else:
            irc.reply(format('Could not find any results for %s.', name))

    def dupe(self, irc, msg, args, text):
        """dupe <search>

        Perform a search for dupe releases using Pre.im's Web API
        """
        limit = self.registryValue('limit', msg.args[0])
        self._dupe(irc, text, limit)
    dupe = wrap(dupe, ['text'])

Class = Dupe