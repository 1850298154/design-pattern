from abc import ABC, abstractmethod

# 抽象表达式类
class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# 终结符表达式类
class TerminalExpression(AbstractExpression):
    def __init__(self, data):
        self.data = data

    def interpret(self, context):
        return self.data in context

# 非终结符表达式类
class OrExpression(AbstractExpression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) or self.expr2.interpret(context)

class AndExpression(AbstractExpression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) and self.expr2.interpret(context)

# 使用示例
def main():
    # 规则：Robert 和 John 是男性
    robert = TerminalExpression("Robert")
    john = TerminalExpression("John")
    is_male = OrExpression(robert, john)

    # 规则：Julie 是一个已婚的女性
    julie = TerminalExpression("Julie")
    married = TerminalExpression("Married")
    is_married_woman = AndExpression(julie, married)

    # 测试
    print("John is male? " + str(is_male.interpret("John")))
    print("Julie is a married woman? " + str(is_married_woman.interpret("Married Julie")))
    print("Robert is male? " + str(is_male.interpret("Robert")))
    print("Julie is male? " + str(is_male.interpret("Julie")))

if __name__ == "__main__":
    main()
"""
John is male? True
Julie is a married woman? True
Robert is male? True
Julie is male? False

----------------------------------------

### 解释

1. **抽象表达式类（AbstractExpression）**：
   - 定义了一个抽象方法 `interpret`，所有具体表达式类都必须实现这个方法。

2. **终结符表达式类（TerminalExpression）**：
   - 实现了 `AbstractExpression` 接口，并在 `interpret` 方法中检查数据是否在上下文中。

3. **非终结符表达式类（OrExpression 和 AndExpression）**：
   - 实现了 `AbstractExpression` 接口，并在 `interpret` 方法中定义了逻辑或和逻辑与操作。

4. **使用示例**：
   - 创建终结符表达式对象 `robert` 和 `john`，并使用 `OrExpression` 创建一个表示男性的表达式 `is_male`。
   - 创建终结符表达式对象 `julie` 和 `married`，并使用 `AndExpression` 创建一个表示已婚女性的表达式 `is_married_woman`。
   - 测试不同的上下文，检查表达式的解释结果。

通过这种方式，解释器模式可以用来定义一个语言的文法，并解释语言中的句子。
    """