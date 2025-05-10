def print_fibonacci(length):
    if length <= 0:
        print("[]")
    elif length == 1:
        print("[0]")
    elif length == 2:
        print("[0, 1]")
    else:
        fib_list = [0, 1]
        for _ in range(2, length):  
            next_number = fib_list[-1] + fib_list[-2]
            fib_list.append(next_number)
        print(f"{fib_list}")
