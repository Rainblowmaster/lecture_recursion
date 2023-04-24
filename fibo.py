
def recursive_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)


def main():
    nth = int(input("Zadej kolikátý člen FP chceš vypočítat:"))
    seq = [recursive_nth_fibo(num) for num in range(nth+1)]
    print(seq)

if __name__ == "__main__":
    main()
