from array import *
# 1. Create an array and traverse.
my_array=array('i',[1,2,3,4,5])
for i in my_array:
    print(i)
# 2. access individual elements through indexs
print(f"Array Value at index 3 : " ,my_array[3])
# 3. Apeend any value to the array useing append () 
my_array.append(4)
print(my_array)
# 4. insert value in an array using insert() method
my_array.insert(3,6)
print(my_array)
# 4.1 Extend python useing extend () method
my_array1=array('i',[10,11,30])
my_array.extend(my_array1)
print(my_array)
# 5. Add items form list into array using fromlist() method
templist=[20,40,44,55]
my_array.fromlist(templist)
print(my_array)
# 6. REmove any array element user remove() method
my_array.remove(20)
print(my_array)

# 7. REmove last element usin remove pop() method
my_array.pop()
print(my_array)
# 8. fetch any element through its index using index() method
print(my_array.index(11))
# 9. Reverse a python array using reverse() method
my_array.reverse()
print(my_array)
# 10. Get array buffer information through buffer_info() method
print(my_array.buffer_info())
# 11. Check for nuber of occureeneces of an element useing count() method
print(my_array.count(4))
# 12.     convert array to string using to string() method
# sringarray=my_array.tostring() # depricated
sringarray=my_array.tobytes()
ints=array("i")
ints.frombytes(sringarray)
print(ints)
# 13. convert array to  a python list with same elements using to list() method
print(my_array.tolist())
# 14. Append a string to char array using fromString () method
# char_array=array('c',[])
# 15. slice elements from an array
print(my_array[1:4])




