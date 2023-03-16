from Logger import Logger
from Model.Set_Digits import Set_Digits


class Ratio_Calculator(Set_Digits):
    def sum(self):
        sum = float(self.var_x) + float(self.var_y)
        Logger.log_data(Logger, "Ratio sum {} + {} = {}"
                        .format(self.var_x, self.var_y, sum))
        return sum

    def difference(self):
        dif = float(self.var_x) - float(self.var_y)
        Logger.log_data(Logger, "Ratio dif {} - {} = {}"
                        .format(self.var_x, self.var_y, dif))
        return dif

    def mult(self):
        mult = float(self.var_x) * float(self.var_y)
        Logger.log_data(Logger, "Ratio mult {} * {} = {}"
                        .format(self.var_x, self.var_y, mult))
        return mult

    def divide(self):
        div = float(self.var_x) / float(self.var_y)
        Logger.log_data(Logger, "Ratio divide {} / {} = {}"
                        .format(self.var_x, self.var_y, div))
        return div