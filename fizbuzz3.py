def fizbuzz3(number: int):
    print(', '.join(['fizzbuzz' if x%15 == 0 else 'buzz' if x%5 == 0 else 'fizz' if x%3 == 0 else str(x) for x in range(1,number)]))

