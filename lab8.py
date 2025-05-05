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
