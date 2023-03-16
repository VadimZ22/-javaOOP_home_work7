from Model.Complex_Calculator import Complex_Calculator
from Model.Ratio_Calculator import Ratio_Calculator
from Model.Set_Digits import Set_Digits
from View.View import View


class Presenter:

    def __init__(self, view: View, calc: Set_Digits):
        self.view = view
        self.calc = calc

    def button_click(self):
        operation = self.view.set_value("С какими числами хотите выполнить операцию:\n" +
                "1 - комплексные\n" +
                "2 - рациональные\n")
        match operation:
            case '1': self.button_click_complex()
            case '2': self.button_click_ratio()

    def button_click_complex(self):
        self.calc = Complex_Calculator()
        self.calc.var_x = self.view.set_value("x: ")
        self.calc.var_y = self.view.set_value("y: ")
        operation = self.view.set_value("Введите операцию:\n" +
                                        "1 - sum\n" +
                                        "2 - mult\n" +
                                        "3 - divide\n" +
                                        "4 - difference\n")

        match operation:
            case '1': self.view.print(self.calc.sum(), "sum result: ")
            case '2': self.view.print(self.calc.mult(), "mult result: ")
            case '3': self.view.print(self.calc.divide(), "divide result: ")
            case '4': self.view.print(self.calc.difference(), "difference result: ")

    def button_click_ratio(self):
        self.calc = Ratio_Calculator()
        self.calc.var_x = self.view.set_value("x: ")
        self.calc.var_y = self.view.set_value("y: ")
        operation = self.view.set_value("Введите операцию:\n" +
                                        "1 - sum\n" +
                                        "2 - mult\n" +
                                        "3 - divide\n" +
                                        "4 - difference\n")

        match operation:
            case '1': self.view.print(self.calc.sum(), "sum result: ")
            case '2': self.view.print(self.calc.mult(), "mult result: ")
            case '3': self.view.print(self.calc.divide(), "divide result: ")
            case '4': self.view.print(self.calc.difference(), "difference result: ")

