from abc import ABCMeta, abstractmethod


# �����Ʒ��ɫ����ʲô���ı���ȥʹ��
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

# ��Ʒ��ɫ
class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei == True:
            print("����֧����{0}Ԫ!".format(money))
        else:
            print("֧�������֧����{0}Ԫ!".format(money))

# ��Ʒ��ɫ
class WechatPay(Payment):
    def pay(self, money):
        print("΢��֧����%dԪ!" % (money))

# �������ɫ
class PaymentFactory:
    def ctreate_payment(self, method):
        if method == 'Alipay':
            return Alipay()
        elif method == 'WechatPay':
            return WechatPay()
        elif method == 'HuabeiPay':
            return Alipay(use_huabei=True)
        else:
            raise TypeError('No such payment named %s' % method)

# �ͻ��˵��á���ֱ����ͻ��˱�¶���󴴽���ʵ��ϸ�ڣ�����ͨ��һ�������������𴴽���Ʒ���ʵ��
pf = PaymentFactory()
p = pf.ctreate_payment('HuabeiPay')
p.pay(100)