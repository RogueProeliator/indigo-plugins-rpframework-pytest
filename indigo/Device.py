class Device(object):

    def __init__(self, device_dfn):
        for k, v in device_dfn.items():
            try:
                setattr(self, k, v)
            except:
                pass

        if not self.sharedProps:
            self.sharedProps = {}
