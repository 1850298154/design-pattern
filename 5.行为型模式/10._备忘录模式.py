# 备忘录类
class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state

# 发起人类
class Originator:
    def __init__(self, state: str):
        self._state = state

    def set_state(self, state: str):
        print(f"Originator: Setting state to {state}")
        self._state = state

    def get_state(self) -> str:
        return self._state

    def save_state_to_memento(self) -> Memento:
        print(f"Originator: Saving state to Memento.")
        return Memento(self._state)

    def get_state_from_memento(self, memento: Memento):
        self._state = memento.get_state()
        print(f"Originator: State after restoring from Memento: {self._state}")

# 管理者类
class Caretaker:
    def __init__(self):
        self._memento_list = []

    def add(self, state: Memento):
        self._memento_list.append(state)

    def get(self, index: int) -> Memento:
        return self._memento_list[index]

# 使用示例
if __name__ == "__main__":
    originator = Originator("State1")
    caretaker = Caretaker()

    originator.set_state("State2")
    caretaker.add(originator.save_state_to_memento())

    originator.set_state("State3")
    caretaker.add(originator.save_state_to_memento())

    originator.set_state("State4")

    print("\nCurrent State:", originator.get_state())
    originator.get_state_from_memento(caretaker.get(0))
    print("First saved State:", originator.get_state())
    originator.get_state_from_memento(caretaker.get(1))
    print("Second saved State:", originator.get_state())


"""

Originator: Setting state to State2
Originator: Saving state to Memento.
Originator: Setting state to State3
Originator: Saving state to Memento.
Originator: Setting state to State4

Current State: State4
Originator: State after restoring from Memento: State2
First saved State: State2
Originator: State after restoring from Memento: State3
Second saved State: State3

--------------------------------------------


### 解释

1. **备忘录类（Memento）**：
   - 保存发起人的内部状态。
   - 提供 `get_state` 方法来获取保存的状态。

2. **发起人类（Originator）**：
   - 有一个内部状态 `_state`。
   - 提供 `set_state` 和 `get_state` 方法来设置和获取状态。
   - 提供 `save_state_to_memento` 方法来保存当前状态到备忘录。
   - 提供 `get_state_from_memento` 方法来从备忘录恢复状态。

3. **管理者类（Caretaker）**：
   - 负责保存和恢复备忘录。
   - 提供 `add` 方法来添加备忘录到列表。
   - 提供 `get` 方法来从列表中获取备忘录。

4. **使用示例**：
   - 创建发起人对象 `originator` 和管理者对象 `caretaker`。
   - 改变发起人的状态，并保存状态到备忘录。
   - 恢复发起人的状态，并打印当前状态和保存的状态。

通过这种方式，备忘录模式可以在不破坏封装性的前提下，捕获和恢复对象的内部状态。




"""