import importlib
import pkgutil
import os

# Iterate over all modules in this package
package_dir = os.path.dirname(__file__)
for (_, module_name, is_pkg) in pkgutil.iter_modules([package_dir]):
    if not is_pkg:
        importlib.import_module(f".{module_name}", package=__name__)