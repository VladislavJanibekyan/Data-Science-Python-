class Money:
    def __init__(self, amount_init,currency_initialization):
            self.amount_init = amount_init
            self.currency_initialization = currency_initialization

    def print_obj(self):
        return print(str(self.amount_init) + self.currency_initialization)
    def sum_mon(self,second_obj):
        self.amount_init = self.amount_init + second_obj.amount_init 
        return self

    def sub_mon(self,second_obj):
        self.amount_init = abs(self.amount_init - second_obj.amount_init)
        return self

def main():
    obj_1 = Money(25, "USD")

    obj_2 = Money(2, "USD")
    obj_1.print_obj()
    obj_2.print_obj()
    obj_1.sum_mon(obj_2).print_obj()
    obj_1.sub_mon(obj_2).print_obj()




main()