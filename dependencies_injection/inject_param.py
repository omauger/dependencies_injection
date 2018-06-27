from dependencies_injection.exceptions import WrongParameterInjected
from functools import wraps
import inject
import inspect
import os
import importlib


class inject_param(object):
    """Decorator to inject parameter in function
    """
    def __init__(self, flag):
        self.flag = flag
        inject.configure_once(
            self.config_wrapper(
                self.get_dependencies_binding(),
            )
        )

    def __call__(self, original_func, *args, **kwargs):
        func_signature = inspect.signature(original_func)
        args_names = func_signature.parameters

        if self.flag not in args_names:
            raise WrongParameterInjected('Unable to inject param "%s" in "%s : %s not in %s"' % (self.flag, original_func.__name__, self.flag, args_names))

        @wraps(original_func)
        def wrapped(*args, **kwargs):
            all_args = kwargs.copy()
            for n, v in zip(args_names, args):
                all_args[n] = v

            if self.flag not in all_args:
                kwargs[self.flag] = inject.instance(self.flag)

            return original_func(*args, **kwargs)

        return wrapped

    @staticmethod
    def config_wrapper(dependencies_binding):
        def config(binder):
            """Inject factory configuration in binder

            :param settings: binder
            :type settings: inject.Binder
            """
            for item in dependencies_binding.items():
                binder.bind_to_constructor(item[0], item[1])

        return config

    @staticmethod
    def get_dependencies_binding():
        modules_list = os.listdir(os.getcwd())
        di_module = None

        if 'di.py' in modules_list:
            di_module = importlib.import_module('di')

        if not di_module:
            submodules_list = {}

            for module in modules_list:
                if os.path.isdir("%s/%s" % (os.getcwd(), module)):
                    submodules_list[module] = os.listdir(
                        "%s/%s" % (os.getcwd(), module)
                    )

            for key in submodules_list.keys():
                if 'di.py' in submodules_list[key]:
                    di_module = importlib.import_module('%s.di' % key)
                    break

        if not di_module:
            raise Exception("Can't import dependencies injection binding. Please create di.py file in project.")

        return getattr(di_module, 'DEPENDENCIES')
