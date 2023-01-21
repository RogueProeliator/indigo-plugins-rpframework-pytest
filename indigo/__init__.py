import json
import os

from Device        import Device
from DevicesList   import DevicesList
from IndigoServer  import IndigoServer
from VariablesList import VariablesList

devices   = DevicesList()
variables = VariablesList()
server    = IndigoServer()


def read_test_data(directory):
    if os.path.isdir(directory):
        for content in os.listdir(directory):
            # the content could be either a folder or a file
            if os.path.isdir(content):
                read_test_data(content)
            else:
                # process this specific file according to the naming convention
                if content.lower().startswith("device"):
                    _read_test_device(content)


def _read_test_device(filename):
    global devices
    try:
        json_file = open(filename)
        dev_data = json.load(json_file)

        if dev_data is dict:
            devices.append(Device(dev_data))
        elif dev_data is list:
            for dev in dev_data:
                devices.append(Device(dev))
    except:
        pass