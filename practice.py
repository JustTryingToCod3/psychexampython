# Assignment 1
print('20% Tip Calculator')
x = float(input('Enter Selling Price: '))
tip= (x*.20) + x
print(tip)

# Assignment 2
x = int(input('month of year'))
if x == 9:
 print('fall')

# Assigment 3
n=int(input())
reverse=0
temp=n
reverse = (reverse*10) + (temp % 10)
print(reverse)

# Assigment 4
x=1 + 1 * 2 + 4 / 5
print(x)


# Assigment 5
control_variable=0
end_loop=50
four,five=[],[]
while control_variable<end_loop:
  if control_variable%5==0:
    five.append(control_variable)
  elif control_variable%4==0:
    four.append(control_variable)
  control_variable += 2
print('five_numbers: ', five)
print('four_numbers: ', four)

# Assigment 6
def display_invoice (username, amount, date):
  print(f'hello {username}')
  print(f'your bill of {amount} is due on {date}')

display_invoice("Motherfucker",42.50,"January 1")

# Assigment 7
number = int(input('enter a value: '))
sum = 0
while number >= 0 and number <=100:
  sum+= number
  number = int(input("enter a value: "))
print("sum is: ",sum)

# Assigment 8
number= int(input("input a value: "))
avg,cnt=0,0
while number>0 and number<100:
  number = (int(input("Input a Value: ")))
  sum+=number
  cnt+=1
  avg=(sum/cnt)
print(avg)

# Assigment 9
number= int(input("input a value: "))
avg,cnt=0,0
while number>0 and number<100:
  number = (int(input("Input a Value: ")))
  sum+=number+cnt
  cnt+=1
  avg=(sum/cnt)
print(avg)

# Assigment 11
x=int(input('Enter your gift budget: '))
y=int(input('Enter the age of the recipient: '))
if x<20 and y<=12:
    print('Toy')
if x<20 and y>=13<=19:
    print('Book')
if x>=20 and y>=20:
    print('Gift Card')
if x>=20 and y>=13>=19:
    print('Board Game')
  
# Assigment 12
def daylight_savings(x,y):
  x=int(input("Month of the year lowercase:"))
  y=int(input("Day of the month lowercase: "))
  if int(x>=3 and x<=11):
    print("Daylight Savings")
  else:
    print("Sunshine All Day!")
daylight_savings(x,y)

# Assigment 13
ages=[19, 20, 21, 22, 19, 17, 33, 45, 22, 18, 20, 19]
cnt, sum= 0, 0
while cnt < len(ages):
  sum+= int(ages[cnt])
  cnt+= 1
avg = round(sum/cnt)
print('Average Age is: ', avg)

# Assigment 14
ages = [1,2,3,4,5,6,7,8,9,10,11,12,56]
number = 1
cnt,sup=0,0
while cnt<len(ages):
  sup+=int(ages[cnt])
  cnt+=1
  avg=round(sup/cnt)
print(avg)

# Assigment 15
s = 'My name is David'
print(s[2:6])
print(s[6:7])
index=7

# Assigment 16
s="My name is barbara"
print(s[::-1])
# Assigment 17
s="My name is tyler"
print(s[-2::-1])

# Assigment 18
ages = [12,23,23,456,2,3,4,5,6,7,8,6,42,564,7,8979,54,2]
cnt,sup=0,0
while cnt<len(ages):
  sup+=int(ages[cnt])
  cnt+=1
  avg=round(sup/cnt)
print(avg)

# Assigment 19
ls = ['1','2','3','4','5','6','7','8','9']
for ls in ls:
  if ls in '3':
    continue
  print(ls[0:10])

# Assigment 20
x=float(input('Principal Amount:'))
y=int(input('Time In Years'))
z=float(input("Rate Of Interest"))
total_amount=((z*12)+x)*y
print(total_amount)

# Assigment 21
n = (str.lower(input("Are You Ready? Yes or No? ")))

while n == "no" and n!='yes':
  print('Come Back again')
  break
  print(n)
  if n== 'yes':
    print("let us begin!")
    break
if n!= 'yes' and n!= 'no':
  print('not valid')

print(n)
