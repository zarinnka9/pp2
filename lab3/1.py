def change(grams):
    return grams * 28.3495231

grams = float(input("Enter the amount in grams: "))
ounces = change(grams)
print(f"{grams} grams is equal to {ounces:.4f} ounces.")
