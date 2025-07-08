def singleton(class_):
    instances = {}
    print(instances)
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
            print(instances)
        return instances[class_]
    return getinstance



@singleton
class A:
    a=1
    pass

obj2 = A()
obj3 = A()

print(id(obj2), id(obj3))