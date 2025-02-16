def square_generator(N):
    for i in range(1, N + 1):
        yield i * i  

N = 10
for square in square_generator(N):
    print(square)
