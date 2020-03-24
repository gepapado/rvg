import numpy as np

def scalar_uniform_dist(dtype, params, shape):
    base_mapping = {
        np.unsignedinteger : lambda l, h, shape: np.random.randint(max(l, 0), h, shape),
        np.signedinteger   : np.random.randint,
        np.floating        : np.random.uniform
    }

    try:
       low, high = params
    except TypeError:
        low, high = -params, params

    return base_mapping[dtype.type.__base__](low, high, shape)

def isstruct(dtype):
    return hasattr(dtype, 'names') and dtype.names
def isscalar(dtype):
    return hasattr(dtype, 'names') and not dtype.names