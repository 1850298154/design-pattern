from abc import ABC, abstractmethod

# 状态接口
class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

# 具体状态类
class ConcreteStateA(State):
    def handle(self, context):
        print("State A handling request and transitioning to State B.")
        context.set_state(ConcreteStateB())

class ConcreteStateB(State):
    def handle(self, context):
        print("State B handling request and transitioning to State A.")
        context.set_state(ConcreteStateA())

# 上下文类
class Context:
    def __init__(self, state: State):
        self._state = state

    def set_state(self, state: State):
        self._state = state

    def request(self):
        self._state.handle(self)

# 使用示例
if __name__ == "__main__":
    # 初始化上下文并设置初始状态
    context = Context(ConcreteStateA())

    # 触发请求，观察状态的变化
    context.request()  # 输出: State A handling request and transitioning to State B.
    context.request()  # 输出: State B handling request and transitioning to State A.
    context.request()  # 输出: State A handling request and transitioning to State B.
    context.request()  # 输出: State B handling request and transitioning to State A.