import sys

a = 0
b = 1

print("Beech leaf-mining weevil")

output = f"{a}, {b}"

try:
    terms = int(sys.argv[1])
except:
    print("Not a number, defaulting to 10")
    terms = 10

for i in range(3, terms + 1):
    a, b = b, a + b
    output += f", {b}"

print(f"The first fibonacci numbers are: {output}")