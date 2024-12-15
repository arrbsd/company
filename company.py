"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]


# 1. Вывести названия всех отделов
print(f"1. Вывести названия всех отделов")
for department in departments:
    print(f'Отдел: {department["title"]}')


# 2. Вывести имена всех сотрудников компании.
print(f"\n2. Вывести имена всех сотрудников компании.")
for department in departments:
    for employee in department['employers']:
       print(f'{employee["first_name"]} {employee["last_name"]}')


# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
print(f"\n3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.")
for department in departments:
    for employee in department['employers']:
       print(f'{employee["first_name"]} {employee["last_name"]} работает в отделе {department["title"]}')


# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
print(f"\n4. Вывести имена всех сотрудников компании, которые получают больше 100к.")
for department in departments:
    for employee in department['employers']:
        if employee["salary_rub"] > 100000:
            print(f"Зарплата у {employee['first_name']} {employee['last_name']} составляет {employee['salary_rub']}")


# 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
print(f"\nВывести позиции, на которых люди получают меньше 80к (можно с повторениями)")
for department in departments:
    for employee in department['employers']:
        if employee['salary_rub'] < 80000:
            print(f"Зарплата на позиции {employee['position']} составляет {employee['salary_rub']}")


# 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
print(f"\nПосчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела")
for department in departments:
    total_sum = sum([employee['salary_rub'] for employee in department['employers']])
    print(f"На {department['title']} тратится {total_sum} рублей в месяц")


# 7. Вывести названия отделов с указанием минимальной зарплаты в нём.
print(f"\nВывести названия отделов с указанием минимальной зарплаты в нём.")
for department in departments:
    min_sal = min([employee['salary_rub'] for employee in department['employers']])
    print(f"Минимальная зарплата в отделе {department['title']} составляет {min_sal} рублей.")


# 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
print(f"\nВывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём")
for department in departments:
    salary_in_dep = [employee['salary_rub'] for employee in department['employers']]
    min_salary = min(salary_in_dep)
    avg_salary = sum(salary_in_dep) / len(salary_in_dep)
    max_salary = max(salary_in_dep)
    print(f"В отделе {department['title']}:\n"
          f"минимальная зарплата составляет {min_salary} рублей\n"
          f"средняя зарплата составляет {avg_salary} рублей\n"
          f"максимальная зарплата составляет {max_salary} рублей\n")


# 9. Вывести среднюю зарплату по всей компании.
print(f"\nВывести среднюю зарплату по всей компании")
total_salary = 0
total_employees = 0
for department in departments:
    salary_in_dep = [employee['salary_rub'] for employee in department['employers']]
    total_salary += sum(salary_in_dep)
    total_employees += len(salary_in_dep)
avg_salary = total_salary / total_employees
print(f"Средняя зарплата в компании составляет {avg_salary} рублей.")


# 10. Вывести названия должностей, которые получают больше 90к без повторений.
print(f"\nВывести названия должностей, которые получают больше 90к без повторений.")
position_titles = set()
for department in departments:
    for employee in department['employers']:
        if employee['salary_rub'] > 90000:
            position_titles.add(employee['position'])
print(f"Зарплата больше 90000 рублей на должности:")
for position_title in position_titles:
    print(f"{position_title}")


# 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
print(f"\nПосчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).")
women_salary = {}
women_count = {}
for department in departments:
    for employee in department['employers']:
        if employee['first_name'] in ['Michelle', 'Nicole', 'Christina', 'Caitlin']:
            if department['title'] not in women_salary:
                women_salary[department['title']] = 0
                women_count[department['title']] = 0
            women_salary[department['title']] += employee['salary_rub']
            women_count[department['title']] += 1
for department_title in women_salary:
    avg_salary = women_salary[department_title] / women_count[department_title]
    print(f"Средняя зарплата девушек отдела {department_title} составляет {avg_salary} рублей.")


# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
print(f"\nВывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.")
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
names = set()
for department in departments:
    for employee in department['employers']:
        if employee['last_name'][-1].lower() in vowels:
            names.add(employee['first_name'])
print("Имена людей, чьи фамилии заканчиваются на гласную букву:")
for name in names:
    print(name)


# 13. Вывести список отделов со средним налогом на сотрудников этого отдела.
print(f"\nВывести список отделов со средним налогом на сотрудников этого отдела.")

# Функция для вычисления налога на сотрудника
def calc_tax(employee, taxes):
    total_tax = 0
    for tax in taxes:
        # Если налог применяется ко всем сотрудникам компании или к сотрудникам указанного отдела
        if tax["department"] is None or tax["department"].lower() == department["title"].lower():
            # Добавляем налог к общей сумме налога
            total_tax += (employee["salary_rub"] * tax["value_percents"]) / 100
    return total_tax

# Словарь для хранения среднего налога отдела
department_taxes = {}
for department in departments:
    total_tax = 0
    number_of_employees = 0
    for employee in department["employers"]:
        # общий налог для отдела
        total_tax += calc_tax(employee, taxes)
        number_of_employees += 1
    # средний налог на одного сотрудника
    try:
        average_tax = total_tax / number_of_employees
    except ZeroDivisionError:
        average_tax = 0
    department_taxes[department["title"]] = average_tax

# список отделов со средним налогом на сотрудников
for department, average_tax in department_taxes.items():
    print(f"Отдел: {department}, Средний налог: {average_tax}")


# 14. Вывести список всех сотрудников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
print(f"\nВывести список всех сотрудников с указанием зарплаты \"на руки\" и зарплаты с учётом налогов.")
for department in departments:
    print(f"Отдел: {department['title']}")
    for employee in department["employers"]:
        # Вычисляем зарплату с учётом налогов
        salary_with_tax = employee["salary_rub"] - calc_tax(employee, taxes)
        print(f"Имя сотрудника: {employee['first_name']} {employee['last_name']}\n"
              f"Должность: {employee['position']}\n"
              f"Зарплата: {employee['salary_rub']}\n"
              f"Зарплата с учетом налога: {salary_with_tax}\n")


# 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
print(f"\nВывести список отделов, отсортированный по месячной налоговой нагрузки.")
department_tax_load = {}
for department in departments:
    total_tax_load = 0
    for employee in department["employers"]:
        # налоговая нагрузка для отдела
        total_tax_load += calc_tax(employee, taxes)
    department_tax_load[department["title"]] = total_tax_load

# сортировка отделов по налоговой нагрузке
sorted_departments = sorted(department_tax_load.items(), key=lambda x: x[1], reverse=True)

for department, tax_load in sorted_departments:
    print(f"Налоговая нагрузка {department} составляет {tax_load}")


# 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
print(f"\nВывести всех сотрудников, за которых компания платит больше 100к налогов в год.")
for department in departments:
    for employee in department["employers"]:
        # сумма налогов на сотрудника в году
        sum_tax_in_year = calc_tax(employee, taxes) * 12
        if sum_tax_in_year > 100000:
            print(f"сотрудник, чей годовой налог больше 100к: {employee['first_name']} {employee['last_name']} "
                  f"({sum_tax_in_year} рублей)")


# 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов
print(f"\nВывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов")
min_tax = float('inf')
min_tax_employee = None
for department in departments:
    for employee in department["employers"]:
        # ежемесячный налог на сотрудника
        month_tax = calc_tax(employee, taxes)
        if month_tax < min_tax:
            min_tax = month_tax
            min_tax_employee = employee

# Выводим информацию о сотруднике с наименьшей суммой налогов
print(f"сотрудник за которого компания платит меньше всего налогов: "
      f"{min_tax_employee['first_name']} {min_tax_employee['last_name']} ({min_tax})")
