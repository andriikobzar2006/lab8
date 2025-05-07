students = {
    1: {
        "група": "КІ-301",
        "ПІБ": "Іваненко Петро Олександрович",
        "курс": 3,
        "успішність": {
            "Математика": 88,
            "Програмування": 92,
            "Історія": 76
        }
    },
    2: {
        "група": "КІ-301",
        "ПІБ": "Сидоренко Марія Василівна",
        "курс": 3,
        "успішність": {
            "Математика": 93,
            "Програмування": 89,
            "Історія": 81
        }
    }
}

def add_student(student_id, group, pib, course, grades):
    students[student_id] = {
        "група": group,
        "ПІБ": pib,
        "курс": course,
        "успішність": grades
    }

add_student(
    student_id=3,
    group="КІ-301",
    pib="Коваль Андрій Миколайович",
    course=3,
    grades={
        "Математика": 75,
        "Програмування": 85,
        "Історія": 78
    }
)

print("Інформація про студентів:\n")
for student_id, data in students.items():
    print(f"ID студента: {student_id}")
    print(f"Група: {data['група']}")
    print(f"ПІБ: {data['ПІБ']}")
    print(f"Курс: {data['курс']}")
    print("Успішність:")
    for subject, grade in data["успішність"].items():
        print(f"  {subject}: {grade}")
    print("-" * 40)

#Sema
students = {
    1: {
        "група": "КІ-301",
        "ПІБ": "Іваненко Петро Олександрович",
        "курс": 3,
        "успішність": {
            "Математика": 88,
            "Програмування": 92,
            "Історія": 76
        },
        "email": "ivanenko@example.com"
    },
    2: {
        "група": "КІ-301",
        "ПІБ": "Сидоренко Марія Василівна",
        "курс": 3,
        "успішність": {
            "Математика": 93,
            "Програмування": 89,
            "Історія": 81
        },
        "email": "sydorenko@example.com"
    }
}


def add_student(student_id, group, pib, course, grades, email=None):
    """Додає нового студента до словника з перевіркою унікальності ID"""
    if student_id in students:
        print(f"Помилка! Студент з ID {student_id} вже існує.")
        return False

    students[student_id] = {
        "група": group,
        "ПІБ": pib,
        "курс": course,
        "успішність": grades,
        "email": email
    }
    return True


def print_students():
    """Виводить інформацію про всіх студентів"""
    print("\nІнформація про студентів:")
    for student_id, data in students.items():
        print(f"\nID студента: {student_id}")
        print(f"Група: {data['група']}")
        print(f"ПІБ: {data['ПІБ']}")
        print(f"Курс: {data['курс']}")
        if data.get('email'):
            print(f"Email: {data['email']}")
        print("Успішність:")
        for subject, grade in data["успішність"].items():
            print(f"  {subject}: {grade}")
        print("-" * 40)


def calculate_average_grade(student_id):
    """Розраховує середній бал студента"""
    if student_id not in students:
        return None
    grades = students[student_id]["успішність"].values()
    return sum(grades) / len(grades)


def sort_by_average_grade():
    """Сортує студентів за середнім балом (за спаданням)"""
    student_avg_grades = []
    for student_id in students:
        avg = calculate_average_grade(student_id)
        student_avg_grades.append((student_id, avg))

    sorted_students = sorted(student_avg_grades, key=lambda x: x[1], reverse=True)

    print("\nРейтинг студентів за середнім балом:")
    for rank, (student_id, avg) in enumerate(sorted_students, 1):
        student = students[student_id]
        print(f"{rank}. {student['ПІБ']}: {avg:.2f} балів")


def find_students_above_average(min_avg):
    """Знаходить студентів з середнім балом вище заданого"""
    print(f"\nСтуденти з середнім балом вище {min_avg}:")
    found = False
    for student_id in students:
        avg = calculate_average_grade(student_id)
        if avg > min_avg:
            found = True
            student = students[student_id]
            print(f"{student['ПІБ']}: {avg:.2f} балів")

    if not found:
        print(f"Немає студентів з середнім балом вище {min_avg}")


add_student(
    student_id=3,
    group="КІ-301",
    pib="Коваль Андрій Миколайович",
    course=3,
    grades={
        "Математика": 75,
        "Програмування": 85,
        "Історія": 78
    },
    email="koval@example.com"
)

print_students()

sort_by_average_grade()

find_students_above_average(85)
