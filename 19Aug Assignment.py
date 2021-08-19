#1)Reverse a String and print it on console
   #"Python Skills" .

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
s = "Python Skills"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string(using loops) is : ",end="")
print (reverse(s))
# 2)Assign String to x variable in DD-MM-YYYY format
  #   extract and print Year from String.
import datetime
date_str = '29/12/2017' # The date - 29 Dec 2017
format_str = '%d/%m/%Y' # The format
datetime_obj = datetime.datetime.strptime(date_str, format_str)
print(datetime_obj.date())

#3)In a small company, the average salary of three employees is Rs1000 per week. If one employee earns Rs1100 and other earns Rs500, how much will the third employee earn? Solve by using java programm
average = 1000
e1 = 1100
e2 = 500

e3 = (average - (e1 + e2)/3)*3                  #Calculating salary of 3rd employee


print("Salary of Third employee is: ", e3)

#4)Write Program - convert a percentage to a fraction (To convert a percentage into fraction let say 30% to a fraction)
per = 50
frac = per / 100

print ("Fraction of 50% is:")
print(frac)

#5)Write Program - A train 340 m long is running at a speed of 45 km/hr. what time will it take to cross a 160 m long tunnel?
 lengthoftrain=340
lengthoftunnel=160
#Total distance to be travelled by train
distance=lengthoftrain+lengthoftunnel
print("Total distance to be travelled by train:",distance,"m")
#conversion of km per hour into min per seconds
speed=45*5/18
print("Speed=",speed,"m/sec")
time=distance/speed
print("Time taken by train to cross the tunnel=",time,"secs") 



