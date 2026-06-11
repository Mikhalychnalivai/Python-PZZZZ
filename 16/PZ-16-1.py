# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения.

class Counter:
    def __init__(self):
        self.value = 0
 
    def increment(self):
        self.value += 1
 
    def decrement(self):
        self.value -= 1
 
 
c = Counter()
print(c.value)
c.increment()
c.increment()
c.increment()
c.increment()
c.increment()
print(c.value)
c.decrement()
c.decrement()
print(c.value)