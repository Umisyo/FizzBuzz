def main():
    i = 0

    while i <= 1000:

        if i % 15 == 0:
            print(str(i) + 'FizzBuzz')

        elif i % 3 == 0:
            print(str(i) + 'Fizz')

        elif i % 5 == 0:
            print(str(i) + 'Buzz')

        else:
            print(str(i))

        i += 1

if __name__ == "__main__":
    main()