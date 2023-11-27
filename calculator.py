def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2
def power(num1,num2):
    return num1**num2
print("please select operation -\n" \
      "1. add\n" \
      "2. subtract\n" \
      "3. multiply\n" \
      "4. divide\n"\
      "5. power\n")
select = int(input("select operation from 1, 2, 3, 4,5:"))

number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))

if select ==1:
    print(number_1, "+", number_2,"=",add(number_1,number_2))

elif select == 2:
    print(number_1,"-",number_2,"=",subtract(number_1,number_2))


elif select == 3:
    print(number_1,"*",number_2,"=",multiply(number_1,number_2))

elif select == 4:
    print(number_1,"/",number_2,"=",divide(number_1,number_2))

elif select == 5:
    print(number_1,"**",number_2,"=",power(number_1,number_2))



else:
    print("invalid input")
 



