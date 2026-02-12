#everything in python is an object

# variable stores references

# id() shows the memeory identity

# immutable

# int
# float
# str
# tuple


#mutable
# list
# dict
# set


a = [1,2]
b=a
print(id(a),id(b))


x = 10
y = x
y = 20
print(x)

a = [1,2]
b = a
b.append(3)
print(a)

# The list is actually a in place modification means chnaging object without creating a new object in memory

# but for the int float etc we will create another object in the memory

                #section 2 
#<------------------------------------------------>

# SECTION 2 – Identity vs Equality
a = [1,2]
b = [1,2]

print(a == b)
print(a is b)


# the "==" operator checks the data inside the objects is the same (two seperate copies of the same book)

# is(identity) --> this check teh variables points to the same memory address (can be used to check the singletons)

                #section 3
#<---------------------------------------------------------->

import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

# Modify a nested element
original[0][0] = "X"

print(original) # [['X', 2], [3, 4]]
print(shallow)  # [['X', 2], [3, 4]]  <-- Affected!
print(deep)     # [[1, 2], [3, 4]]    <-- Safe!



                #section 4
#<---------------------------------------------------------->
# 2. Why State PersistsBecause that list is created at definition time, every time you call the 
# function without providing an argument, you are reusing that exact same list object in 
# memory.Pythonprint(func()) # Output: [1]
# print(func()) # Output: [1, 1]
# print(func()) # Output: [1, 1, 1]
# Since lists are mutable, the append(1) operation modifies that "shelf" in-place. 
# The next call doesn't get a new list; it gets the same list, now slightly heavier with the previous call's data.3. How to Fix It SafelyTo avoid this "leaky" behavior, you use None as a placeholder. This works because None is immutable. 
# You cannot "append" to None or change it; you can only replace it.The Safe Version:Pythondef func(a=None):
if a is None:
    a = []  # A brand new list is created inside the function's scope
    a.append(1)
return a
# Why this is safe:Fresh Object: The a = [] line only runs when the function is actually executed. 
# This ensures a brand-new list is created in a fresh memory slot every single time.Explicit Check: 
# Using if a is None: is the standard "Pythonic" way to handle optional mutable arguments.Summary Table for 
# InterviewsFeatureMutable Default (a=[])Safe Default (a=None)Creation TimeAt function definition (Once)
# At function execution (Every time)MemoryShared across all callsUnique to each callCommon UseAlmost n
# ever (unless caching)Industry standard



                #section 5
#<---------------------------------------------------------->





# 1. What is "Pass-by-Object-Reference"?When you pass a variable into a function, Python passes the reference to the object, not a copy of the object itself. However, the behavior you see depends entirely on whether that object is mutable or immutable.The Assignment Rule: Inside a function, the parameter name (like lst) becomes an alias for the object passed in.The Modification Rule: If you modify that object in-place (like append), the change is visible outside. If you reassign the name (like lst = [9, 9]), you break the link to the original and 
# point to something new.2. Practice AnalysisPythondef modify(lst):
#     lst.append(5)  # Modifying the object in-place

# a = [1, 2]
# modify(a)
# print(a) # Output: [1, 2, 5]
# What happened here?Variable a points to a list object [1, 2] in memory.When modify(a) is called, t
# he local function variable lst is pointed to that exact same memory address.lst.append(5) 
# finds the list at that address and adds a 5 to it.Because a is still looking at that same address, 
# it "sees" the new number when the function finishes.3. The Reassignment Twist (Interview Curveball)Look what happens if we change the function slightly:Pythondef modify_v2(lst):
#     lst = [10, 20] # REASSIGNMENT

# a = [1, 2]
# modify_v2(a)
# print(a) # Output: [1, 2]
# Why didn't a change?When you use the = operator inside the function, you aren't changing the list [1, 2]. 
# You are telling the local name lst to stop looking at a's list and start looking at a brand new list [10, 20]. The original list a remains untouched.Comparison SummaryActionEffect on Original VariableWhy?lst.append(x)ChangesIn-place modification of a shared object.lst[0] = xChangesIn-place modification of a shared object.lst = [x, y]No ChangeReassignment; the local name points to a new address.x = x + 1 
# (int)No ChangeIntegers are immutable; math always creates a new object.


# There is inplace and Rebinding

# a = [1,2]

# a+=[3] --> This method is exactly like the .extend  operator it change on the existing object

# a = a + [3]. --> This method create another memory slot by combining a and [3]



# for list += --> in-place mutation
# Tuple.  --> Rebinding(new object created)

