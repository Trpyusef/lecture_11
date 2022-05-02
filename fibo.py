def recrusive_nth_fibo(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return recrusive_nth_fibo(n-1) + recrusive_nth_fibo(n-2)
def main():
    print(recrusive_nth_fibo(5))


if __name__ == "__main__":
    main()
