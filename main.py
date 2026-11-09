students_db = [
    {"id": 1, "name": "Алексей", "grades": [5, 4, 5, 3]},
    {"id": 2, "name": "Мария", "grades": [4, 5, 4]},
    {"id": 3, "name": "Иван", "grades": []},
    {"id": 4, "name": "Ольга", "grades": [3, 2, 3, "4"]},
]


def get_average_grade(student):
    # Считает средний балл студента
    return sum(student["grades"]) / len(student["grades"])


def find_student_by_id(student_id):
    # Ищет студента по ID
    for student in students_db:
        if str(student["id"]) == student_id:
            return student
    return None


def generate_new_id():
    # Генерирует новый уникальный ID: максимальный существующий ID + 1.
    # Не зависит от длины списка, поэтому после удаления студентов ID не дублируются.
    if not students_db:
        return 1
    return max(student["id"] for student in students_db) + 1


def add_new_student(name, grades_str):
    # Добавляет нового студента. Оценки передаются строкой через запятую (например: '4,5,3')
    try:
        if not grades_str.strip():
            raise ValueError ("Пустая строка")
        grades = [int(g.strip()) for g in grades_str.split(",")]
    except ValueError:
        print("Ошибка: оценки должны быть числами через запятую, например: 4,5,3")
        return

    new_id = generate_new_id()
    new_student = {"id": new_id, "name": name, "grades": grades}
    students_db.append(new_student)
    print(f" Студент {name} успешно добавлен с ID {new_id}!")


def delete_student(student_id):
    #Удаление студента с заданным id
    for st in students_db:
        if st["id"] == int(student_id):
            students_db.remove(st)


def print_report():
    # Выводит красивый отчет по всем студентам
    print("\n--- ОТЧЕТ УСПЕВАЕМОСТИ ---")
    for student in students_db:
        avg = get_average_grade(student)
        print(f"[{student['id']}] {student['name']} | Средний балл: {avg:.2f}")


def main():
    while True:
        print("\n Меню:")
        print("1. Показать отчет")
        print("2. Найти студента по ID")
        print("3. Добавить студента")
        print("4. Удалить студента")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print_report()
        elif choice == "2":
            sid = input("Введите ID студента: ")
            student = find_student_by_id(sid)
            if student:
                print(f"Найдено: {student['name']}, Оценки: {student['grades']}")
            else:
                print("Студент не найден")
        elif choice == "3":
            name = input("Имя студента: ")
            grades = input("Оценки через запятую (например: 4,5,3): ")
            add_new_student(name, grades)
        elif choice == "4":
            s_id = input("Введите ID студента: ")
            delete_student(s_id)
        elif choice == "5":
            break
        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()
