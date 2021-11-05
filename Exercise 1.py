
number = int(input("Welcome, enter a number: " ))
sum = 0
if number % 2 == 0 :
    for i in range(1, number + 1):
        sum = sum +i
    print("the sum is: ", sum)
else:
    for i in range(1, number + 1, 2):
        sum = sum +i
        average = sum / number
    print("The average is: ", average)





