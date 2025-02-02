def solve(heads, legs):
    for chic in range(heads + 1): 
        rab = heads-chic 
        if (chic*2+rab*4) == legs: 
            return chic, rab
    return "No solution"
heads = 35
legs = 94
chic, rab = solve(heads, legs)
print(f"Chickens: {chic}, Rabbits: {rab}")
