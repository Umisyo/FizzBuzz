def main():
    i = 0

    while i < 1000:
        Fizz = i % 3
        Buzz = i % 5

        if Fizz == 0 and Buzz != 0:
            print(str(i) + 'Fizz')

        elif Fizz != 0 and Buzz == 0:
            print(str(i) + 'Buzz')

        elif Fizz == 0 and Buzz == 0:
            print(str(i) + 'FizzBuzz')

        else:
            print(str(i))

        i += 1

if __name__ == "__main__":
    main()