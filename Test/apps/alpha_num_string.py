import random, string
x = ''.join(random.choice(string.ascii_letters) for _ in range(16))
print(x)