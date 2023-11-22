while True:
    try:
        n = int(input())
        result = '1' * len(str(n))
        while int(result) % n != 0:
            result += '1'
        print(len(result))
    except:
        break