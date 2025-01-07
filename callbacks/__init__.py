
import importlib 
import os
def register_callbacks(app):
    dir = os.path.dirname(__file__)
    for file_name in os.listdir(dir):
        if file_name != "__init__.py":
            module_name = f"callbacks.{file_name[:-3]}"
            module = importlib.import_module(module_name)
            module.register(app)
 