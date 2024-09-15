from abc import ABCMeta, abstractmethod

# ------��Ʒ------
class Player:
    def __init__(self, face=None, body=None, arms=None, legs=None):
        self.face = face
        self.body = body
        self.arms = arms
        self.legs = legs

    def __str__(self):
        return '%s,%s,%s,%s' % (self.face, self.body, self.arms, self.legs)

# ------��������------
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arms(self):
        pass

    @abstractmethod
    def build_legs(self):
        pass

# ------���彨����,������һ����Ʒ���ڲ��ṹ------
class GirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = 'Ư��������'

    def build_body(self):
        self.player.body = '���������'

    def build_arms(self):
        self.player.arms = 'ϸϸ�ĸ첲'

    def build_legs(self):
        self.player.legs = '����'

# ------���彨���ߣ���ʾ����------
class MonsterBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '����'

    def build_body(self):
        self.player.body = '���������'

    def build_arms(self):
        self.player.arms = '��׳�ĸ첲'

    def build_legs(self):
        self.player.legs = '��׳�Ĵ���'

# ------ָ���ߣ��������(�������ͱ�ʾ����ֿ�)�����ԶԹ�����̽��и��Ӿ�ϸ�ؿ���------
class PlayerDirectory():
    def builder_player(self, builder):
        """
        ������װ�����
        :param builder:
        :return:
        """
        builder.build_face()
        builder.build_body()
        builder.build_arms()
        builder.build_legs()
        return builder.player

# ------�ͻ���------
builder = GirlBuilder()
director = PlayerDirectory()
p = director.builder_player(builder)
print(p)  # Ư��������,���������,ϸϸ�ĸ첲,����