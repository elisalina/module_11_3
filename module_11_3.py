from inspect import getmodule

def introspection_info(obj):
    return {'type': type(obj).__name__,
            'attribures': obj.__dict__,
            'methods': dir(obj),
            'module': getmodule(obj).__name__}

class MyClass:
    pass
obj = MyClass()

number_info = introspection_info(obj)
print(number_info)
