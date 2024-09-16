from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "Product A"

class ConcreteProductB(Product):
    def operation(self):
        return "Product B"

class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self):
        product = self.factory_method()
        return product.operation()

class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# 使用示例
if __name__ == "__main__":
    creator_a = ConcreteCreatorA()
    print(creator_a.some_operation())  # 输出: Product A

    creator_b = ConcreteCreatorB()
    print(creator_b.some_operation())  # 输出: Product B