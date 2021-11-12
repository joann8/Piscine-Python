import my_minipack.progressbar
import my_minipack.logger
from time import sleep

listy = range(1000)
ret = 0
for elem in my_minipack.progressbar(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)

listy = range(3333)
ret = 0
for elem in my_minipack.progressbar(listy):
	ret += elem
	sleep(0.005)
print()
print(ret)
