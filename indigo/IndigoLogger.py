import logging

logging.addLevelName(5, "THREADDEBUG")
logging.THREADDEBUG = 5

class IndigoLogger(logging.Logger):
    def threaddebug(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.THREADDEBUG):
            self._log(logging.THREADDEBUG, msg, args, **kwargs)
