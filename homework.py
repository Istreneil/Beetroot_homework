student_fields = ['first_name', 'last_name', 'age', 'email', 'address', 'gender']

STUDENTS = []

TEST_STUDENTS = [
    ['Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F'],
    ['John', 'S', 'new_mail@mail.com', '21', 'London', 'M'],
    ['Andy', 'H', 'more_mail@mail.com', 'sexteen', 'Brighton', 'M']
]

def add_student():
    student = {}
    for field in student_fields:
        field = field.capitalize().replace('_', ' ') #чудово вийшло використати цей рядок до функції адд, і тепер кожного нового студента воно додає так, як ти просила
        student[field] = input('Enter {}\t'.format(field))
        if field == 'age':
            try:
                int(student['age'])
            except:
                student['age'] = input('Enter age as number\t')
    STUDENTS.append(student)

def calculate_avg_age():
    try:
        total_age = 0
        for student in STUDENTS:
            total_age += int(student['age'])
        avgerage_age = total_age / len(STUDENTS)
        print('Average age is {}'.format(avgerage_age))
    except ValueError:
        print('Cannot calculate average age')
    except Exception as e:
        print(str(e))

def print_student(student):
    for field in student:
        print(field, '\t', student[field])

def print_students_list():
    for student in STUDENTS:
        print_student(student)
        print('\t')


def load_students():
    for test_student in TEST_STUDENTS:
        STUDENTS.append(dict(zip(student_fields, test_student)))


while True:
    action = input('Desired action:\t')
    if action == 'add':
        add_student()
    elif action == 'load':
        load_students()
    elif action == 'print':
        print_students_list()
    else:
        break