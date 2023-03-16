from Logger import Logger
from Model.Set_Digits import Set_Digits


class Complex_Calculator(Set_Digits):
    def sum(self):
        sum = complex(self.var_x) + complex(self.var_y)
        Logger.log_data(Logger, "Complex sum {} + {} = {}"
                        .format(self.var_x, self.var_y, sum))
        return sum

    def difference(self):
        dif = complex(self.var_x) - complex(self.var_y)
        Logger.log_data(Logger, "Complex difference {} - {} = {}"
                        .format(self.var_x, self.var_y, dif))
        return dif

    def mult(self):
        mult = complex(self.var_x) * complex(self.var_y)
        Logger.log_data(Logger, "Complex mult {} * {} = {}"
                        .format(self.var_x, self.var_y, mult))
        return mult

    def divide(self):
        div = complex(self.var_x) / complex(self.var_y)
        Logger.log_data(Logger, "Complex div {} / {} = {}"
                        .format(self.var_x, self.var_y, div))
        return div