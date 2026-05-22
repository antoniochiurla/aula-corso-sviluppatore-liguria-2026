import time

amount = 100000

def first_opt():
    start_time = time.time()

    even_numbers = []
    for n in range(amount):
        if n % 2 == 0:
            even_numbers.append(n)

    print(f"Elapsed first function : {time.time() - start_time}")

def second_opt():
    start_time = time.time()

    even_numbers = [n if n % 2 == 0 else 0 for n in range(amount)]

    print(f"Elapsed second function: {time.time() - start_time}")

def main():
    for fun in [first_opt, second_opt]:
        fun()


if __name__ == "__main__":
    main()