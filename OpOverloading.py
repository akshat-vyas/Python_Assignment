#OPERATOR OVERLOADING
class complex:
 def _init_(self, a, b):
 self.a = a
 self.b = b
 # adding two objects
 def _add_(self, other):
 return self.a + other.a, self.b + other.b
Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)
