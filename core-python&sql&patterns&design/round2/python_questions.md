q1) a = [1,2,3]
b = a
b.append(4)

print(a)

b is pointing to the same addessing so here the mutation is happens so the answer will be [1,2,3,4]

q2)

a = [1,2,3]
b = a[:]

a.append(4)

print(b)

here append is also a mutation and b will be start a new address location as we are slicing it so the b will be [1,2,3]

q3)

 one is whether the values are same or not but he is is acually checking the memeory identity
