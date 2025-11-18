def singleton(class_):
    print("Entry point")
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
    a = 1
    pass


obj1 = A()
obj2 = A()
obj3 = A()
obj4 = A()
