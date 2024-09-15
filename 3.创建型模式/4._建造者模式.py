from abc import ABCMeta, abstractmethod

# ------����Ĳ�Ʒ------
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass

class PhoneCPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class PhoneOS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass
        
# ------����Ĳ�Ʒ------
class SmallShell(PhoneShell):
    def show_shell(self):
        print('��ͨ�ֻ�С�ֻ���')

class BigShell(PhoneShell):
    def show_shell(self):
        print('��ͨ�ֻ����ֻ���')

class AppleShell(PhoneShell):
    def show_shell(self):
        print('ƻ���ֻ���')

class SnapDragonCPU(PhoneCPU):
    def show_cpu(self):
        print('����CPU')

class HuaweiCPU(PhoneCPU):
    def show_cpu(self):
        print('��ΪCPU')

class AppleCPU(PhoneCPU):
    def show_cpu(self):
        print('ƻ��CPU')

class AndroidOS(PhoneOS):
    def show_os(self):
        print('IOSϵͳ')

class AppleOS(PhoneOS):
    def show_os(self):
        print('��׿ϵͳ')

# ------����Ĺ���------
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

# ------����Ĺ���------
class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()

    def make_cpu(self):
        return HuaweiCPU()

    def make_os(self):
        return AndroidOS()

class AppleFactory(PhoneFactory):
    def make_shell(self):
        return AppleShell()

    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return AppleOS()

# ------�ͻ���------
class Phone:
    def __init__(self, shell, cpu, os):
        self.shell = shell
        self.cpu = cpu
        self.os = os

    def show_info(self):
        print('�ֻ���Ϣ��')
        self.shell.show_shell()
        self.cpu.show_cpu()
        self.os.show_os()

def make_phone(factory):
    shell = factory.make_shell()
    cpu = factory.make_cpu()
    os = factory.make_os()
    return Phone(shell, cpu, os)

p = make_phone(HuaweiFactory())
p.show_info()
"""
�ֻ���Ϣ��
��ͨ�ֻ�С�ֻ���
��ΪCPU
IOSϵͳ
"""