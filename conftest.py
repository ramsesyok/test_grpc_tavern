import re
from tavern.testutils.pytesthook import hooks as _tavern_hooks
from tavern.testutils.pytesthook.file import YamlFile as _YamlFile

def _patched_collect_file(parent, path):
    match_tavern_file = re.compile(r".+\.tavern\.ya?ml$").match
    if path.basename.startswith("test") and match_tavern_file(path.strpath):
        return _YamlFile.from_parent(parent=parent, path=path)
    return None

# override Tavern's outdated collector to support newer pytest versions
_tavern_hooks.pytest_collect_file = _patched_collect_file
