import random
import sys

def generate_expression():
    ops = ['+', '-', '*', '/']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(ops)
    return f"{num1},{op},{num2}", eval(f"{num1} {op} {num2}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_data.py <amount_of_data> <output_file>")
        sys.exit(1)

    data_len = int(sys.argv[1])
    output_file = sys.argv[2]

    data = [generate_expression() for _ in range(data_len)]

    with open(output_file, 'w') as f:
        for expression, result in data:
            f.write(f"{expression},{result}\n")
