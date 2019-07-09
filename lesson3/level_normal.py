file = open('salary_file.txt', 'w', encoding='utf-8')

people = ['Иван', 'Василий', 'Аркадий', 'Николай', 'Дмитрий', 'Алексей', 'Анатолий', 'Игорь']
salaries = [35000, 67000, 42000, 52000, 49000, 39000, 30000, 55000]
lib_salary = dict(zip(people, salaries))

for key, value in lib_salary.items():
    file.write(key + ' - ' + str(value) + '\n')
file.close()

file = open('salary_file.txt', 'r', encoding='UTF-8')
for line in file:
    name, dash, salary = line.split()
    if int(salary) <= 50000:
        salary_tax = int(salary) * 0.87
        print(name.upper(), dash, salary_tax)
file.close()

