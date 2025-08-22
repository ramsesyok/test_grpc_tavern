import pykwalify.core as _pkc
if not hasattr(_pkc, 'yaml') and hasattr(_pkc, 'yml'):
    _pkc.yaml = _pkc.yml
