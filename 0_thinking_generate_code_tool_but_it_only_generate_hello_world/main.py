import random

file_name = input()

with open(file_name, "w") as f:
    f.write(random.randint(1, 100) * "print(\"Hello, World!\")\n")