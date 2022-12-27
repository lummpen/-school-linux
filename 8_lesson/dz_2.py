#!/usr/bin/python3
class Animals: # Класс животные

    def __init__(self, animal_species, origin, habitat) -> None:
        self.animal_species = animal_species # Вид животных(млекопиающие, земноводные и тд)
        self.origin = origin # Происхождение
        self.habitat = habitat #Место обитания


class Mammals(Animals): # Класс млекопитающие
 
    def __init__(self, animal_species, origin, habitat, mammal_species,
                 gender, name, age, height, weight):
        super().__init__(animal_species, origin, habitat)
        self.mammal_species = mammal_species # Вид
        self.gender = gender # пол
        self.name = name # имя
        self.age = age # возраст
        self.height = height # рост
        self.weight = weight # вес


class Human(Mammals):

    def __init__(self, animal_species, origin, habitat, mammal_species, gender, name,
                 age, height, weight, profession, marital_status, hobby):
        super().__init__(animal_species, origin, habitat, mammal_species,
                         gender, name, age, height, weight)
        self.profession = profession # профессия
        self.marital_status = marital_status # семейное положение
        self.hobby = hobby # хоби
        
        def say(self):
            print('ha-ha')

class Student(Human):

    def __init__(self, animal_species, origin, habitat, mammal_species, gender,
                 name, age, height, weight, profession, marital_status, hobby,
                 speciality, num_course, count_executed_works):
        super().__init__(animal_species, origin, habitat, mammal_species, gender,
                         name, age, height, weight, profession, marital_status, hobby)
        self.speciality = speciality # специальность
        self.num_course = num_course # номер курса
        self.count_executed_works = count_executed_works # кооличество сданных ДЗ


Dasha = Student('Mammals', 'Eurasia', 'Northern part of Eurasia', 'Human', 'female',
                'Dasha', 19, 168, 60, 'student', 'unmarried', 'read boks', 'programmer', 3, 15)
Vova = Student('Mammals', 'Eurasia', 'Northern part of Eurasia', 'Human', 'male',
               'Vova', 21, 190, 85, 'student', 'unmarried', 'play videogame ', 'programmer', 4, 10)
Alexander = Student('Mammals', 'Latin America', 'Northern part of Eurasia', 'Human', 'male',
              'Alexander', 20, 185, 75, 'student', 'unmarried', 'sport', 'programmer', 3, 13)

print(f'{Dasha.name} находится на курсе {Dasha.speciality}')
print('Сдала домашних заданий:', Dasha.count_executed_works)
print(f'{Vova.name} находится на курсе {Vova.speciality}')
print('Сдал домашних заданий:', Vova.count_executed_works)
print(f'{Alexander.name} находится на курсе {Alexander.speciality}')
print('Сдал домашних заданий:', Alexander.count_executed_works)
