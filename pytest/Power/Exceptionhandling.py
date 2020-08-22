try:
    a = int(input("Enter 1st number"))
    b  = int(input("Enter 2nd number"))
    print(a/b)

except ZeroDivisionError as e:
    print("Division by zero not possible")
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print("Something Went Wrong...",e)

finally:
    print("End")