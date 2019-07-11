while True:
    num = int(input('Номер задания: '))
    if num == 1:
        list = [1, 2, 4, 0]
        result = [i**2 for i in list]
        print(result)
    elif num == 2:
        list_1 = ['яблоко', 'ананас', 'апельсин', 'манго']
        list_2 = ['ананас', 'груша', 'яблоко', 'персик']
        result = [fruit for fruit in list_1 if fruit in list_2]
        print(result)
    elif num == 3:
        list_num = [2, 4, 65, 44, 98, 67, 9, 18, 21]
        result = [number for number in list_num if number % 3 == 0 and number > 0 and number % 4 != 0]
        print(result)
    elif num == 0:
        break