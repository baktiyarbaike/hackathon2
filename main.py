from views import *
import json

class Cars(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    def save(self):
        while True:
            print('1 - Создание записей\n2 - Получения списка записей\n3 - Получения записи одной\n4 - Обновления записей\n5 - Удаления записей')
            inp_ = int(input('Выберите действие: (1,2,3,4,5): '))
            if inp_ == 1: 
                print(super().create_car())
            elif inp_ == 2: 
                print(super().listing_all_of_cars())
            elif inp_ == 3: 
                print(super().retrieve_car())
            elif inp_ == 4: 
                print(super().update_car())
            elif inp_ == 5: 
                print(super().delete_car())
            else:
                print('Такого действия нет!')
            inp_ = input('Вы хотите продолжить? Да/Нет: ').lower()
            if inp_ == 'да':
                self.save()
            else:
                print('До свидания!')
            break
inp_ = Cars()
inp_.save()
