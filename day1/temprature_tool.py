#logic:F=(C*9/5)+32
print("Temprature Rearch Tool")
try:
    celcius=float(input("Enter temprature in celcius:"))
    fahrenheit=(celcius*9/5)+32
    print(f"{celcius}°c is Equal to:{fahrenheit}°f")

except ValueError:
     print("Error: Enter a valid number.Letter are not allowed.")

    

   