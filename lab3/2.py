def change(F):
    return (5/9)*(F - 32)

F = float(input("Enter the temp in Fahrenheit "))
C = change(F)
print(f"{F} Fahrenheit is equal to {C:.2f} centrigate.")