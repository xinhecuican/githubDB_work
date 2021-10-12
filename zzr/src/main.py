import importlib
import logging
import sys

from PyQt5.QtWidgets import QApplication

from zzr.src.Helper import Window_manager
from zzr.src.Helper.Register import Register, Registers
from zzr.src.MainWindow import MainWindow


def _handle_errors(errors):
    """Log out and possibly reraise errors during import."""
    if not errors:
        return
    for name, err in errors:
        logging.warning("Module {} import failed: {}".format(name, err))


ALL_MODULES = [("zzr.src", ["MainWindow"]),
               ("zzr.src.User_info", ["User_info_panel"]),
               ("zzr.src.Repository_info", ["Repository_panel"]),
               ("zzr.src", ["Table_panel"])]


def import_all_modules_for_register(custom_module_paths=None):
    """Import all modules for register."""
    modules = []
    for base_dir, module in ALL_MODULES:
        for name in module:
            full_name = base_dir + "." + name
            modules.append(full_name)
    if isinstance(custom_module_paths, list):
        modules += custom_module_paths
    errors = []
    for module in modules:
        try:
            importlib.import_module(module)
        except ImportError as error:
            errors.append((module, error))
    _handle_errors(errors)


if __name__ == "__main__":
    import_all_modules_for_register()
    app = QApplication(sys.argv)
    Window_manager.change_window("MainWindow")
    sys.exit(app.exec_())
