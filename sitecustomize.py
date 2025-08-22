import pykwalify.core as _pkc

# pykwalify<1.8 uses 'yaml' attribute, but newer versions renamed it to 'yml'.
# Ensure compatibility by mapping the attribute if required.
if not hasattr(_pkc, "yaml") and hasattr(_pkc, "yml"):
    _pkc.yaml = _pkc.yml

# Tavern's pytest plugin is written for older pytest versions and directly
# instantiates ``YamlFile`` during collection. Pytest 7+ expects plugins to use
# ``from_parent`` instead, otherwise an error is raised. Patch the plugin at
# import time so that Tavern tests can be collected under newer pytest
# releases.
try:  # pragma: no cover - best effort patching
    import re
    from tavern.testutils.pytesthook import hooks as _tavern_hooks
    from tavern.testutils.pytesthook.file import YamlFile as _YamlFile

    def _patched_collect_file(parent, path):
        match_tavern_file = re.compile(r".+\.tavern\.ya?ml$").match
        if path.basename.startswith("test") and match_tavern_file(path.strpath):
            return _YamlFile.from_parent(parent=parent, path=path)
        return None

    _tavern_hooks.pytest_collect_file = _patched_collect_file
except Exception:
    # If Tavern is not installed, just ignore – normal pytest behaviour will
    # continue without Tavern support.
    pass
