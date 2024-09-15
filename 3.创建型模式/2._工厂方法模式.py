from abc import ABCMeta, abstractmethod

# 抽象产品角色
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

# 具体产品角色
class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei == True:
            print("花呗支付了{0}元!".format(money))
        else:
            print("支付宝余额支付了{0}元!".format(money))

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付了%d元!" % (money))

# 抽象工厂角色
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

# 具体工厂角色
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)

hfp = HuabeiFactory().create_payment()
hfp.pay(100)  # 花呗支付了100元!