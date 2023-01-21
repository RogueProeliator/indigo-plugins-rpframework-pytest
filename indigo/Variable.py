class Variable(object):

    def __init__(self, var_id, var_name, value, global_props=None):
        self.id          = var_id
        self.name        = var_name
        self.value       = value
        self.sharedProps = global_props if global_props else {}