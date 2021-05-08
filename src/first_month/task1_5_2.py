class Money:
    def __init__(self, amount_init:int,currency_initialization:str):
            self.amount_init = amount_init
            try:
                self.amount_init +=1
            except:
                self.amount_init = int(input("please enter valid amount"))
            if self.amount_init < 0:
                self.amount_init = int(input("it can not be negative, give positive"))
            self.currency_initialization = currency_initialization


    def __repr__(self):
        return str(self.amount_init) + self.currency_initialization
    def __add__(self,other):
        result = self.amount_init + other.amount_init 
        return Money(result,self.currency_initialization)

    def __sub__(self,other):
        result = abs(self.amount_init - other.amount_init)
        return Money(result,self.currency_initialization)

def main():
    obj_1 = Money(-3, "USD")
    obj_2 = Money(2, "USD")
    print(obj_1)
    print(obj_2)
    print(obj_1 + obj_2)
    print(obj_1 - obj_2)
    
  





main()