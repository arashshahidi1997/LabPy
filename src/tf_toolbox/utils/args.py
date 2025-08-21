"""Argument defaults and shared constants."""
DEFAULT_FS = 1250.0  # Hz
DEFAULT_TAPERS = (3, 5)

def DefaultArgs(args_dict, defaults):
    """Update args_dict with defaults where missing (MATLAB parity)."""
    out = dict(defaults)
    out.update({k:v for k,v in (args_dict or {}).items() if v is not None})
    return out
