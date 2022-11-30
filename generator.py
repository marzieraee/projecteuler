def f(n):
    yield n%2
    yield n//2
    yield n**2

div = f(6)
print(list(div))
print(type(div))