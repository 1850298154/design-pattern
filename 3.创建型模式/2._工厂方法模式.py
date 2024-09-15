from abc import ABCMeta, abstractmethod

# �����Ʒ��ɫ
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

# �����Ʒ��ɫ
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

# ���󹤳���ɫ
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

# ���幤����ɫ
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
hfp.pay(100)  # ����֧����100Ԫ!