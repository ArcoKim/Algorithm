while True:
    try:
        n = int(input())
        num = 1
        result = 1
        while num % n != 0:
            num = num * 10 + 1
            result += 1
        print(result)
    except:
        break