# Напишите генератор отмазок преподам
import random

class Prof:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.seen_excuses = []

    def add_excuse(self, excuse):
        self.seen_excuses.append(excuse)

class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

def get_student():
    name = input("Введите имя:")
    email = input("Введите email:")
    return Student(name, email)

def choose_prof(profs):
    for (idx, prof) in enumerate(profs):
        print(f"{idx} - {prof.name} {prof.email}")
    while True:
        n_prof = input("Введите номер препода:")
        if not n_prof.isdigit():
            print("Введите число, а не чушь!")
            continue
        n_prof = int(n_prof)
        if n_prof >= len(profs):
            print("Плохой номер препода :(")
            continue
        return profs[n_prof]

class ExcuseGenerator:
    def __init__(self, excuses):
        self.excuses = excuses

    def generate(self, prof):
        if len(prof.seen_excuses) >= len(self.excuses):
            return None
        while True:
            excuse = random.choice(self.excuses)
            if excuse in prof.seen_excuses:
                continue
            prof.add_excuse(excuse)
            return excuse

def send_message(excuse, prof, student):
    print(f"""
    Здравствуйте, {prof.name}!

    К сожалению, я не смогу прийти на пару, поскольку {excuse}. Мне очень жаль.

    С уважением, студентка {student.name}.
    """)

def main():
    profs = [Prof("Artemiy", "artfly94@gmail.com"), Prof("Alexey", "alexey.menzorov@g.nsu.ru"), Prof("Бочаров", "idontlikeyou@yandex.ru")]
    student = get_student()
    excuses = [
        "потоп в Кении",
        "я самбистка",
        "меня закрыли в квартире",
        "красивое Северное сияние, ослепла",
        "меня украли, памагите",
        "у меня свадьба",
        "у Лизы свадьба",
        "я в туалете",
        "у подруги день рождения"
    ]
    generator = ExcuseGenerator(excuses)
    while True:
        prof = choose_prof(profs)
        excuse = generator.generate(prof)
        send_message(excuse, prof, student)

main()