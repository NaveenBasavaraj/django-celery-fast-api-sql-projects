# special functions which can be written in one line

# Passing single or two values
multiply = lambda x,y:x*y
power = lambda x,y:x**y

# passing multiple values or iterators 

nums = [2,4,6,8]
double = list(map(lambda x:x+x, nums))
print(f"multiply function: {multiply(2,3)}")
print(f"power function: {power(2,3)}")

words = ["hello", "world", "hello", "programming"]
words_upper = list(map(lambda x:x.upper(), words)) # str.upper(x)
print(f"{double} is double of {nums}")
print(f"{words_upper} is after capitalising of {words}")

# sorting data using lambda

nums_unsorted = [10,8,32,45,97,12]
nums_us = [50,35,98,782154,248,78,61]
#  print(f"sorted nums which returns new list {sorted(nums_unsorted, reverse=True)}")
nums_unsorted.sort()#reverse = True
print(f"in place sort {nums_unsorted}")
print(f"nums_us is {nums_us}")
nums_us.sort(key=lambda x:x*1.5)
print(f"nums_us sorted based on key {nums_us}")
    

class_att = [("9Z",35), ("9X",10),("9A",27),("9S",33),("9B",40),("9D",90),("9Y",88)]
new_sorted_class_att = sorted(class_att, key = lambda x:x[0])
print(f"sorted class_at {new_sorted_class_att}")


attendance = [36,39,32,30,33,35,37]

print(list(filter(lambda x:x>=35, attendance)))

    
    