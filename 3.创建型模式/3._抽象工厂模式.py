from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei == True:
            print("����֧����{0}Ԫ!".format(money))
        else:
            print("֧�������֧����{0}Ԫ!".format(money))

class WechatPay(Payment):
    def pay(self, money):
        print("΢��֧����%dԪ!" % (money))

class BankPay(Payment):
    def pay(self, money):
        print("����֧����%dԪ!" % (money))

# ������Ʒ�Ĺ�����Ľӿ�
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

# ������
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

# ������
class WechatPayPayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

# ������
class HuabeiPayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)

# ����������֧���Ĺ�����
class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()

bfp = BankPayFactory().create_payment()
bfp.pay(100)  # ����֧����100Ԫ!