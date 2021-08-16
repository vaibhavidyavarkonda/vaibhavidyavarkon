##Find ASCII value of a character 'X' 'x'
S='X'
N='x'
print("The ASCII value of S is",ord(S))

print("The ASCII value of N is",ord(N))

##write a program to compute quotient and remainder
a,b=divmod(10,20)
print("\nquotient of : ",a)
print("\nremainder of :",b)

##swap two numbers using temporary variable
x = 11
y = 21
temp = x
x = y
y = temp
print("\n the value of x :", x)
print("\n the value of y :", y)

## write a program to check whether  a number is even or odd - 88,37,1658
N=88
if(N%2)==0:
  print("\n even number",N)
else:
    print("\n odd number",N)

S=37
if(S%2)==0:
    print("\n even number",S)
else:
    print("\n odd number",S)

V=1658
if(V%2)==0:
    print("\n even number",V)
else:
    print("\n odd number",V)

##check whether an alphabet is vowel or constant using if..else statement - a,b,e,o
l= input("\n Enter a charater")

if l in ('a','e','o'):
        print("\n %s is a vowel."%l)
else:
        print("\n %s is a constant."%l)

##write program to calculate GST i.e 18% on base price 34900
N=34900
GST=0.18*N
print("\n GST is=",GST)


##write a program to calculate monthly simple intrest and compound intrest(5%/month)on amount 161258
a=161258
r=5
t=1
simpleintrest =a*r*t*0.01
print("\n simple intrest is=",simpleintrest)
amount = a * (pow((1 + r / 100),t))
compoundintrest=amount-a
print(" compound intrest is =",compoundintrest)

##write program to generate equated monthly instalments (EMI)(intrest 5% /month) of 3 year and 5 year of amount 161258/-
a=161258
e3=a/36
e5=a/60
emi3=e3+(0.05*e3)
emi5=e3+(0.05*e5)
print("EMI for 3 years with intrest 5%",emi3)
print("EMI for 5 years with intrest 5%",emi5) 

