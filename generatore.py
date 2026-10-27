def conta_fino_a_tre():
    yield 1
    yield 2
    yield 3

for num in conta_fino_a_tre():
    print(num)
