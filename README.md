# Dependencies Injection

This package permit to implement easily dependencies injection in python projects.

You have to define in your project di.py file which describe the DEPENDENCIES binding.

di.py example :
```python

def injected_class():
	from module_to_inject import  ClassToInject
	return ClassToInject

DEPENDENCIES = {
	"injected_class": injected_class, 
}
```

To use the injection in your code, import inject_param decorator and add decorator with string for injected param binding.
Example :
```python
from dependencies_injection.inject_param import inject_param

class A:

	@inject_param("injected_class")
	def func_to_do_something(injected_class=None):
		return injected_class.__class__.__name__
```

You can also inject function or value with the same way.