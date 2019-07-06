while True:

    num = int(input('Введите номер задания: '))

    if num == 1:
        fruits = ["яблоко", "банан", "киви", "арбуз"]
        right_offset = len(max(fruits, key = len))

        for index, item in enumerate(fruits, start=1):
            result = '{}. {}'.format(index, item.rjust(right_offset))
            print(result)

    elif num == 2:
        s1 = [1, 2, 3]
        s2 = [3, 5, 6]
        s1 = [x for x in s1 if x not in s2]
        print(s1)


    elif num == 3:
        s = [34, 21, 12, 38, 95, 76, 41, 65]
        i = 0
        while i < len(s):
            if s[i] % 2 == 0:
                print(s[i] / 4)
                i += 1
            else:
                print(s[i] * 2)
                i += 1
    else:
        break


