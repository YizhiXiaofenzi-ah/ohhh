with open("5000_lines_print_hello_world.py", "w") as f:
    for i in range(5000):
        f.write(f"print(\"Hello, World!\") #{i + 1}\n")