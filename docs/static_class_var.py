class MyClass:
    class_var = 'original'  # class_or_static_variable
obj1 = MyClass()
obj2 = MyClass()
obj1.class_var = 'modified'
print(obj1.class_var)  # Output: 'modified'
print(obj2.class_var)  # Output: 'original'
print(MyClass.class_var)  # Output: 'original'
class CSStudent: # Class for Computer Science Student
    stream = 'cse'                  # class_or_static_variable
    def __init__(self,roll,name):
        self.roll = roll            # instance_variable
        self.name = name            # instance_variable

# Objects of CSStudent class
a = CSStudent(1,'mayańk')
b = CSStudent(2,'ԃilαvr')

print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.name)    # prints "mayańk"
print(b.name)    # prints "ԃilαvr"
print(a.roll)    # prints "1"
print(b.roll)    # prints "2"

print(CSStudent.stream) # prints "cse"
a.stream = 'ece'
print(a.stream) # prints 'ece'
print(b.stream) # prints 'cse'
print(CSStudent.stream) # prints "cse"
CSStudent.stream = 'mech'
print("point_to_note: ",a.stream) # prints 'ece'
print(b.stream) # prints 'mech'