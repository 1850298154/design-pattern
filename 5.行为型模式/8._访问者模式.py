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
        s = element.operation_a()
        print(f"{s} + ConcreteVisitor1")

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
"""
The client code works with all visitors via the base Visitor interface:
ConcreteElementA + ConcreteVisitor1
ConcreteElementB + ConcreteVisitor1

It allows the same client code to work with different types of visitors:
ConcreteElementA + ConcreteVisitor2
ConcreteElementB + ConcreteVisitor2

It allows the same client code to work with different types of visitors:
ConcreteElementA + ConcreteVisitor2
ConcreteElementB + ConcreteVisitor2
ConcreteElementA + ConcreteVisitor2
ConcreteElementB + ConcreteVisitor2
ConcreteElementB + ConcreteVisitor2




---------------------------------------



### 解释

1. **访问者接口（Visitor）**：
   - 定义了两个抽象方法 `visit_concrete_element_a` 和 `visit_concrete_element_b`，所有具体访问者类都必须实现这些方法。

2. **具体访问者类（ConcreteVisitor1 和 ConcreteVisitor2）**：
   - 实现了 `Visitor` 接口，并在 `visit_concrete_element_a` 和 `visit_concrete_element_b` 方法中定义了具体的操作。

3. **元素接口（Element）**：
   - 定义了一个抽象方法 `accept`，所有具体元素类都必须实现这个方法。

4. **具体元素类（ConcreteElementA 和 ConcreteElementB）**：
   - 实现了 `Element` 接口，并在 `accept` 方法中调用访问者的相应方法。
   - 定义了各自的操作方法 `operation_a` 和 `operation_b`。

5. **客户端代码（client_code）**：
   - 接受一个元素列表和一个访问者对象，并对每个元素调用其 `accept` 方法。

6. **使用示例**：
   - 创建具体元素对象列表 `elements`。
   - 创建具体访问者对象 `visitor1` 和 `visitor2`。
   - 调用 `client_code` 函数，展示访问者模式的效果。

通过这种方式，访问者模式将操作与对象结构分离，使得可以在不改变对象结构的情况下定义新的操作。



"""