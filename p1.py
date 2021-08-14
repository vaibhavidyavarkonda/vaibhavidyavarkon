#Write a program to manipulate List data

A=['c',','C++','JAVA','python','Html',1,2,3,4,5]
print("List A :",A[:])

print("List A : 2 to 5",A[2:6])

print("List A in reverse:",A[::-1])

A.append('Name')
print("List A after appending  :",A[:])

A.insert(3,'Java')
print("List A after inserting  :",A[:])

A.pop(1)
print("List A after poping :",A[:])


A.remove('python')
print("List A after removing :",A[:])

del A[0]
print("List A after deleteing :",A[:])

A.clear()
print("List A after clearing :",A[:])