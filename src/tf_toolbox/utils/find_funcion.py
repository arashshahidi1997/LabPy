import pkgutil
import importlib
import inspect
import tf_toolbox

def find_function(func_name):
    package = tf_toolbox
    matches = []

    # Iterate through all submodules of the package
    for loader, module_name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        try:
            module = importlib.import_module(module_name)
            
            # Inspect all functions in the module
            for name, obj in inspect.getmembers(module, inspect.isfunction):
                if name == func_name:
                    matches.append(f"{module_name}.{name}")
        except Exception as e:
            print(f"Skipping {module_name}: {e}")

    return matches