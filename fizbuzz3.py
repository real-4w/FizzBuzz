def fizbuzz3():
    print('\n'.join(['fizzbuzz' if x%15 == 0 else 'buzz' if x%5 == 0 else 'fizz' if x%3 == 0 else str(x) for x in range(1,101)]))

fizbuzz3()