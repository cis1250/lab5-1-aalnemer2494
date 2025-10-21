#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)


def get_positive_integer():
    while True:
        s = input("How many Fibonacci terms do you want? ")
        if s.isdigit():
            n = int(s)
            if n > 0:
                return n
            else:
                print("Error: please enter a number greater than 0.")
        else:
            print("Error: please enter a positive whole number (e.g., 5).")

def generate_fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def print_sequence(seq):
    print("Fibonacci sequence:", " ".join(str(x) for x in seq))

def main():
    n = get_positive_integer()
    seq = generate_fibonacci(n)
    print_sequence(seq)

if __name__ == "__main__":
    main()
