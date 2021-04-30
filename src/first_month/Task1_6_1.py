import task1_3_1  
# Data members - 
# numenator - integer(համարիչ)
# denumerator - integer(հայտարար)

# Data Methods
# Constructor - not only assign values to data member, but also simplify, 
# For example if we have an object obj = Rational(6,8), should create an object with values (3,4).
# se GCD algorithm, for simplifying.



# Ոչ միայն պետք է ուղղակի վերագրի համարիչի և հայտարարի արժեքները, այլ նաև պետք է
 # պարզեցնի այն, օրինակ Rational(6,8) ֊ի դեպքում պետք է սարքի օբյեկտ համապատասխան (3,4) 
 # արժեքներով։ Պարզեցման համար օգտվել ամենամեծ ընդհանուր բաժանարարի ֆունկցիայից։  
# 	__repr__
# 	__add__
# 	__sub__
# 	__mul__
# 	__div__
# 	__eq__
# 	__gt__
# 	__gte__
# 	__lt__
# 	__lte__
# 	__pow__

class Rational:
	def __init__(self,numenator,denumenator):
		
		self.numenator = int(numenator)
		self.denumenator = int(denumenator)
	@classmethod
	def simp(cls, numenator,denumenator):
		num_simp = task1_3_1.gcd(numenator, denumenator)
		return cls(numenator/num_simp,denumenator/num_simp)
	
	def __repr__(self):
		return str(self.numenator) +"  " + str(self.denumenator)
	@staticmethod
	def lcm(numenator,denumenator):
		greater = 0
		wh_br = True
		if numenator > denumenator:
			greater = numenator
		else:
			greater = denumenator

		while wh_br:
			if greater % denumenator == 0 and greater % numenator == 0:
				wh_br = False
				greater -= 1
			greater +=1
		return greater 
	def __add__(self,other):
		x = self.lcm(self.denumenator,other.denumenator)
		y = self.numenator * (x/self.denumenator) + other.numenator * (x / other.denumenator)
		return Rational(y, x)

	def __sub__(self,other):
		x = self.lcm(self.denumenator,other.denumenator)
		y = self.numenator * (x/self.denumenator) - other.numenator * (x / other.denumenator)
		return Rational(y, x)

	def __mul__(self,other):
		x = self.numenator * other.numenator
		y = self.denumenator * other.denumenator
		return Rational(x, y )
	def __truediv__(self,other):
		x = self.numenator * other.denumenator
		y = self.denumenator * other.numenator
		return Rational(x, y)
	def __eq__(self,other):
		if self.numenator == other.numenator and self.denumenator == other.denumenator:
			return True
		else:
			return False
	def __gt__(self,other):
		if self.numenator / self.denumenator > other.numenator / other.denumenator:
			return True
		else:
			return False

	def __ge__(self,other):
		if self.numenator / self.denumenator >= other.numenator / other.denumenator:
			return True
		else:
			return False
	def __lt__(self,other):
		if self.numenator / self.denumenator < other.numenator / other.denumenator:
			return True
		else:
			return False
	def __le__(self,other):
		if self.numenator / self.denumenator <= other.numenator / other.denumenator:
			return True
		else:
			return False
	def __pow__(self,other):
		x = (self.numenator**other.numenator)**(1/other.denumenator)
		y = (self.denumenator**other.numenator)**(1/other.denumenator)
		return Rational(x,y)
obj = Rational.simp(6,8)
obj_1 = Rational.simp(2,3)

print(obj ** obj_1)









