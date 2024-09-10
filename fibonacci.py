import sys

a = 0
b = 1

output = f"{a}, {b}"
terms = int(sys.argv[1])

for i in range(3, terms + 1):
    a, b = b, a + b
    output += f", {b}"

print(output)