print('Фабрика функций')
def create_operation(operation):
    if operation == "mul":
        def mul(x, y):
            return x * y
        return mul
    elif operation == "truediv":
        def truediv(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                return 'Error: Division by zero is not allowed.'
        return truediv
my_func_1 = create_operation('mul',)
my_func_2 = create_operation('truediv')
print(my_func_1 (8,2))
print(my_func_2(4,2))

print('лямбда функция')
multiply = lambda x, y: x * y
print(multiply(5, 7))
def multiply_def(x, y):
   return x * y
print(multiply_def(5,7))
#
print('вызываемый объект')

class Rect:
   def __init__(self, a, b):
       self.a, self.b = 5, 2
   def __call__(self,n):
       return self.a * self.b


rect = Rect(5, 2)
print(f"Стороны: {rect.a}, {rect.b}")
print(f"Площадь:{rect(2)}")

