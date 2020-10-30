def fizzbuzz(max_num):
    counter = 0
    for num in range(1, max_num+1):
        if int(num % 3) == 0 and int(num % 5) == 0:
            print('FizzBuzz')
        elif int(num % 3) == 0:
            print('Fizz')
        elif int(num % 5) == 0:
            print('Buzz')
        else:
            print(num)
        counter += 1

fizzbuzz(15)