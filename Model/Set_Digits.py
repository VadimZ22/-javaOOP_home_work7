
class Set_Digits:

    def __init__(self):
        self.__x = 0
        self.__y = 0

    @property
    def var_x(self):
        return self.__x

    @var_x.setter
    def var_x(self, i):
        self.__x = i

    @property
    def var_y(self):
        return self.__y

    @var_y.setter
    def var_y(self, i):
        self.__y = i



# sd = Set_Digits()
# print(sd.x)
# sd.x = 1
# print(sd.x)

