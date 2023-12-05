def peel(some_class):
    list_of_fun = dir(some_class)
    public_fun = {item for item in list_of_fun if not item.startswith('__')}
    return (public_fun)


class AbstractBase:
    def some_method(self):
        pass


class Base(AbstractBase):
    def some_other_method(self):
        pass


class Closeable(Base):
    def close(self):
        pass


print(peel(Closeable))  # {"some_method", "some_other_method", "close"}


def implements(interface):
    def wrapper(checked_func):
        # print(checked_func.__name__)
        func_methods = peel(checked_func)
        for method in peel(interface):
            assert method in func_methods, f'method \'{method}\' not implemented'
    return wrapper


class Closeable:
    def close(self):
        pass


@implements(Closeable)  # гуд - пусто
class FileReader:
    # ...
    def close(self):
        self.file.close()


@implements(Closeable)  # не сработает ассерт
class Noop:
    pass
