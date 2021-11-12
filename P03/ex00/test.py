from NumPyCreator import NumPyCreator

npc = NumPyCreator()

print("******** TEST 1 ***********")
to_print = npc.from_list([[1,2,3],[6,3,4]]) 
print(to_print)

print("******** TEST 2 ***********")
to_print = npc.from_list([[1,2,3],[6,4]])
print(to_print)

print("******** TEST 3 ***********")
to_print = npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]) 
print(to_print)

print("******** TEST 4 ***********")
to_print = npc.from_list(((1,2),(3,4))) 
print(to_print)

print("******** TEST 5 ***********")
to_print = npc.from_tuple(("a","b","c")) 
print(to_print)

print("******** TEST 6 ***********")
to_print = npc.from_tuple([[1,2,3],[6,3,4]]) 
print(to_print)

print("******** TEST 7 ***********")
to_print = npc.from_iterable(iter(range(5))) 
print(to_print)


print("******** TEST 8 ***********")
shape=(3,5)
to_print = npc.from_shape(shape)
print(to_print)

print("******** TEST 9 ***********")
to_print = npc.random(shape)
print(to_print)

print("******** TEST 10 ***********")
to_print = npc.identity(4)
print(to_print)


