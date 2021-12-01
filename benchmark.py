import fizbuzz1 as f1
import fizbuzz2_oo as f2
import fizbuzz3 as f3
import timer

from timer import Timer
t = Timer()
print("Option 1")
t.start()
f1.fizzbuzz(100)
t.stop()

print("Option 2")
t.start()
ob2 = f2.Solution()
print(ob2.fizzBuzz2(100))
t.stop()

print("Option 3")
t.start()
f3.fizbuzz3()
t.stop()