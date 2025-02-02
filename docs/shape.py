""" python does not have interfaces in the same way as languages like zava or c#. 
however, you can achieve similar functionality using abstract base classes (abc's)
from the abc module. here's why:
duck typing: python embraces the concept of "duck typing", which means that the
type of an object is determined by its behavior rather than its explicit type.
if an object behaves like a duck (i.e., it has the required methods), it is
considered a duck. this allows for **flexible polymorphism** without the need
for **strict interface enforcement**.
ABCs: abstract base classes provide a way to define a common structure for classes,
including abstract methods that must be implemented by subclasses. this allows you to
define a kind of "interface" that ensures certain methods are present in any class
that inherits from the ABC.
Example: shape.py """
from abc import ABC, abstractmethod
import math
class acl_shape(ABC):
    @abstractmethod
    def area(self):
        pass

class cl_square(acl_shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class cl_circle(acl_shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Using the interface
shapes = [cl_square(5), cl_circle(3)]
for shape in shapes:
    print(shape.area())

""" Key Points:
no interface keyword like in java:
unlike other languages, python doesn't have a dedicated keyword for interfaces.
enforcement:
ABCs enforce the implementation of abstract methods, ensuring that subclasses
adhere to the defined structure.
flexibility:
python's duck typing allows for more dynamic and flexible interactions between objects,
even without explicit interfaces. """