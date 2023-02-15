import pkgutil
import inspect

def get_service_modules():
    """
    Get a list of modules used by the microservice.

    Returns:
        A list of module names.
    """
    package_name = 'your_microservice_package_name'  # Replace with the name of your microservice's package
    package_path = __import__(package_name).__path__
    module_names = [name for _, name, _ in pkgutil.iter_modules(package_path)]
    modules = []
    for module_name in module_names:
        try:
            module = __import__(f"{package_name}.{module_name}", fromlist=[""])
            if inspect.ismodule(module):
                modules.append(module)
        except ImportError:
            pass
    return modules
