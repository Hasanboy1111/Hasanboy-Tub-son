def is_prime(n):

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Murakkab son "
    return "Tub son"

if __name__ == "__main__":

    num = int(input("Enter number: "))

    answer = is_prime(num)

    print(answer)

    