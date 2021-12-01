import fizbuzz1 as f1
import fizbuzz2_oo as f2
import fizbuzz3 as f3
from timer import Timer
number = 100

t = Timer()
print("Option 1")
t.start()
f1.fizzbuzz(number)
t.stop()

print("Option 2")
t.start()
ob2 = f2.Solution()
print(ob2.fizzBuzz2(number))
t.stop()

print("Option 3")
t.start()
f3.fizbuzz3(number)
t.stop()