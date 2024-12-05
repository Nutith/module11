from threading import Thread


def introspection_info(obj):
    attributes = dict()
    methods = []
    result = dict()

    result['type'] = obj.__class__.__name__
    result['module'] = getattr(type(obj), '__module__', None)

    for attr_name in dir(obj):
        # пропускаем атрибуты и методы начинающиеся и заканчивающиеся на '__' для чистоты вывода
        # если необходим весь список необходимо закомментировать следующие две строки
        if attr_name.startswith('__') and attr_name.endswith('__'):
            continue

        attr = getattr(obj, attr_name)

        if callable(attr):
            methods.append(attr_name)
        else:
            attributes[attr_name] = attr

    result['attributes'] = attributes
    result['methods'] = methods

    return result


class A:
    def __init__(self):
        self.model = 'fh 1009'
        self.sn = 'A03945804434'

    def process(self):
        pass


class B(A):
    def __init__(self):
        self.price = 924232
        A.__init__(self)

    def postfix(self):
        pass


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self, name=name)
        self.id = 2143


def main():
    ab = B()
    mth = MyThread('sr9')
    th = Thread(name='as9001')
    var_number = 34

    print(introspection_info(ab))
    print(introspection_info(mth))
    print(introspection_info(th))
    print(introspection_info(var_number))
    print(introspection_info('case'))
    print(introspection_info(42))


if __name__ == '__main__':
    main()
