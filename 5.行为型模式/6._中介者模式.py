from abc import ABC, abstractmethod

# 中介者接口
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

# 具体中介者类
class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component2 = component2
        self._component1.set_mediator(self)
        self._component2.set_mediator(self)

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()

# 基础组件类
class BaseComponent:
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator

# 具体组件类
class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A.")
        self._mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 does B.")
        self._mediator.notify(self, "B")

class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C.")
        self._mediator.notify(self, "C")

    def do_d(self):
        print("Component 2 does D.")
        self._mediator.notify(self, "D")

# 使用示例
if __name__ == "__main__":
    component1 = Component1()
    component2 = Component2()
    mediator = ConcreteMediator(component1, component2)

    print("Client triggers operation A.")
    component1.do_a()

    print("\nClient triggers operation D.")
    component2.do_d()

"""
Client triggers operation A.
Component 1 does A.
Mediator reacts on A and triggers following operations:
Component 2 does C.

Client triggers operation D.
Component 2 does D.
Mediator reacts on D and triggers following operations:
Component 1 does B.
Component 2 does C.
        
--------------------------------------------------
### 解释

1. **中介者接口（Mediator）**：
   - 定义了一个抽象方法 `notify`，所有具体中介者类都必须实现这个方法。

2. **具体中介者类（ConcreteMediator）**：
   - 实现了 `Mediator` 接口，并在 `notify` 方法中处理不同的事件。
   - 持有组件的引用，并在组件之间协调交互。

3. **基础组件类（BaseComponent）**：
   - 定义了一个 `_mediator` 属性和一个 `set_mediator` 方法，用于设置中介者。

4. **具体组件类（Component1 和 Component2）**：
   - 继承自 `BaseComponent`，并在其方法中调用中介者的 `notify` 方法来通知事件。

5. **使用示例**：
   - 创建组件对象 `component1` 和 `component2`。
   - 创建中介者对象 `mediator`，并将组件对象传递给它。
   - 触发组件的方法，观察中介者如何协调组件之间的交互。

通过这种方式，中介者模式将组件之间的交互逻辑集中到一个中介者对象中，从而减少了组件之间的直接依赖，提高了系统的可维护性和可扩展性。
        """