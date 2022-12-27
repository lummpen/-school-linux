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

class Cat(Mammals):

    def __init__(self, animal_species, origin, habitat, gender, name,
                 age, height, weight, breed, cat_view):
        super().__init__(animal_species, origin, habitat, gender,
                         name, age, height, weight)
        self.breed = breed # порода
        self.cat_view = cat_view # вид

    def say(self):
        print('Mur-Mur')


class Dog(Mammals):

    def __init__(self, animal_species, origin, habitat, gender, name,
                 age, height, weight, breed, dog_view):
        super().__init__(animal_species, origin, habitat, gender,
                         name, age, height, weight)
        self.breed = breed # порода
        self.dog_view = dog_view # вид

    def say(self):
        print('gav-gav')