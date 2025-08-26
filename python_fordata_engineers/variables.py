my_var = "Rashmi"
last_name = "Mohapatra"
x = 10
y = 5
print(my_var + last_name)
print(f'x+y = {x+y}')

#  multiple assignments

a, b, c = 1, 2, 3
''' here is the comment
I am building a print statement '''
print(f'a = {a}, b = {b}, c = {c}')

# multi line code

total_sum = 10+20+30 \
            +50+60
print(total_sum)

'''indentation'''

var = 1
if(var == 1):
      print("wow")

'''typecasting'''

a = 10
b = "10"
print(type(b))

b_new = int(b)
# explicit typecasting

print(type(b_new))


# implicit typecasting

a = 10

b = 10.5

print(type(b))

print(a+b)

'''String slicing'''
x = "RashmiMohapatra"

print(x[0])

print(x[1])
#  print first 4 char
print(x[:4])

#  pick specific char from h to p
print(x[3:11])

#  0: n (length of the string)
print(x[:])

print(x[:len(x)])


'''string methods'''

print(x.upper())
print(x.lower())
print(x.title())
print(x.find("Mohapatra"))
print(x.replace("Rashmi", "Liti"))

x = "Rashmi Mohapatra"
my_list = x.split(" ")
print(my_list)

file = "raw_data.csv"

if file.endswith(".csv"):
    print("This is a CSV file")

if file.startswith("raw_"):
    print("This is a raw data file")


file = "raw_data.orc"

if file.endswith(".csv"):
    print("This is a CSV file")


statement = "Hello Rashmi. What are you doing today. Hey Rashmi I am talking with you ."

print(statement.count("Rashmi"))

demo_str = "Hello"
demo_var = "10"

print(demo_str.isnumeric())

print(demo_var.isnumeric())

print(demo_var.isalnum())

'''conditional statements'''

if demo_var.isnumeric():
    print("demo_var is numeric")
else:
    print("demo_var is not numeric")


x = 110

if (x == 10):
  print("x is 10")

elif(x >100):
      if(x >100 & x<200):
            print("Between 100 and200")
      print("x is greater than 100")
else:
  print("x is not 10")
