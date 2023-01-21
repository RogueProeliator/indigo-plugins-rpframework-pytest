#! /usr/bin/env python
import logging
from IndigoLogger import IndigoLogger


class PluginBase(object):

    def __init__(self, plugin_id, plugin_name, plugin_version, plugin_prefs):
        self.pluginPrefs = plugin_prefs

        logging.setLoggerClass(IndigoLogger)
        self.logger = logging.getLogger("Plugin")

    def deviceCreated(self, dev):
        pass

    def deviceUpdated(self, old_dev, new_dev):
        pass

    def deviceDeleted(self, dev):
        pass

    def variableCreated(self, var):
        pass

    def variableUpdated(self, old_var, new_var):
        pass

    def variableDeleted(self, var):
        pass
