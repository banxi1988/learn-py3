import collections


def test_init_subclass():
    """
    与类装饰器的区别，类装饰器只影响指定的类，而 `__init_subclass__` 影响所有子类.
    @since 3.6
    """

    class PluginBase:
        subclasses = []

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.subclasses.append(cls)

    class Plugin1(PluginBase):
        pass

    class Plugin2(PluginBase):
        pass

    assert len(PluginBase.subclasses) == 2
    assert PluginBase.subclasses[0] == Plugin1
    assert PluginBase.subclasses[1] == Plugin2


def test_metaclass_example():
    """
    测试使用 collections.OrderedDict 来保存类变量的定义顺序 。
    关于元类的，更多说明请参考:
    https://www.python.org/dev/peps/pep-3115/
    """

    class OrderedClass(type):
        @classmethod
        def __prepare__(metacls, name, bases, **kwargs):
            """
             此 hook 返回一个类似字典的数据结构，用在保存类的成员定义。
            """
            return collections.OrderedDict()

        def __new__(cls, name, bases, namespace, **kwargs):
            result = type.__new__(cls, name, bases, dict(namespace))
            result.members = tuple(namespace)
            return result

    class A(metaclass=OrderedClass):
        def one(self):
            pass

        def two(self):
            pass

        def three(self):
            pass

    members = list(A.members)
    one_index = members.index("one")
    two_index = members.index("two")
    three_index = members.index("three")
    assert one_index < two_index
    assert two_index < three_index
    assert A.members == ("__module__", "__qualname__", "one", "two", "three")

