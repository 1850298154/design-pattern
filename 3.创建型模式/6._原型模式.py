import copy
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class ConcretePrototype1(Prototype):
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"ConcretePrototype1(field1={self.field1}, field2={self.field2})"

class ConcretePrototype2(Prototype):
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"ConcretePrototype2(field1={self.field1}, field2={self.field2})"

# 使用示例
if __name__ == "__main__":
    prototype1 = ConcretePrototype1("value1", [1, 2, 3])
    prototype2 = ConcretePrototype2("value2", {"key": "value"})

    clone1 = prototype1.clone()
    clone2 = prototype2.clone()

    print(prototype1)
    print(clone1)
    print(prototype2)
    print(clone2)

    # 修改原型对象，验证克隆对象是否独立
    prototype1.field1 = "new_value1"
    prototype1.field2.append(4)
    prototype2.field1 = "new_value2"
    prototype2.field2["new_key"] = "new_value"

    print("After modifying the prototypes:")
    print(prototype1)
    print(clone1)
    print(prototype2)
    print(clone2)