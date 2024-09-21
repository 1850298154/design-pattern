from abc import ABC, abstractmethod

# 访问者接口
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass

# 具体访问者类
class ConcreteVisitor1(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"{element.operation_a()} + ConcreteVisitor1")

    def visit_concrete_element_b(self, element):
        print(f"{element.operation_b()} + ConcreteVisitor1")

class ConcreteVisitor2(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"{element.operation_a()} + ConcreteVisitor2")

    def visit_concrete_element_b(self, element):
        print(f"{element.operation_b()} + ConcreteVisitor2")

# 元素接口
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

# 具体元素类
class ConcreteElementA(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_element_a(self)

    def operation_a(self):
        return "ConcreteElementA"

class ConcreteElementB(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_element_b(self)

    def operation_b(self):
        return "ConcreteElementB"

# 客户端代码
def client_code(elements, visitor):
    for element in elements:
        element.accept(visitor)

# 使用示例
if __name__ == "__main__":
    elements = [ConcreteElementA(), ConcreteElementB()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client_code(elements, visitor1)

    print("\nIt allows the same client code to work with different types of visitors:")
    visitor2 = ConcreteVisitor2()
    client_code(elements, visitor2)