num = int(input("Enter an integer >= 2: "))

if num >= 2:
    for i in range(2, num + 1):
        if num % i == 0:
            break
        else:
            i += 1
    print(f"The smallest factor other than 1 for {num} is {i}.")
    
else:
    print("Invalid input. Enter a number greater than 2.")
