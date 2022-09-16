import json

FILE = 'data.json'

class Mixin:
    def get_data(self):
        with open(FILE) as file:
            return json.load(file)

    def get_id(self):
        with open('id.txt','r') as file:
            id = int(file.read())
            id += 1
        with open('id.txt', 'w') as file2:
            file2.write(str(id))
        return id

class CreateMixin(Mixin):
    def create_car(self):
        data = super().get_data()
        try:
            new_car = {
                'id': super().get_id(),
                'brand': input('Введите марку машины: '), 
                'model': input('Введите модель машины: '), 
                'year_of_issue': int(input('Введите год выпуска машины: ')), 
                'engine_volume': round(float(input('Введите объем двигателя машины: ')),1), 
                'color': input('Введите цвет машины: '),
                'body_type': input('Выберите тип кузова (седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап): '),
                'mileage': int(input('Введите пробег машины: ')),
                'price': round(float(input('Введите цену машины: ')),2)
            }
        except ValueError:
            print('Введите корректные данные!')
            self.create_car()
        else:
            data.append(new_car)
            with open(FILE,'w') as file:
                json.dump(data, file)
            return 'УСПЕШНО СОЗДАНО!'
class ListingMixin(Mixin):
    def listing_all_of_cars(self):
        print('Это список машин')
        data = super().get_data()
        print(data)
        return 'Конец!'

class RetrieveMixin(Mixin):
    def retrieve_car(self):
        data = super().get_data()
        try:
            id = int(input('Введите id машины: '))
        except ValueError:
            print('Введите корректные данные!')
            return self.retrieve_car()
        else:
            _car = list(filter(lambda x: x['id'] == id, data))
            if not _car: return 'Нет такой машины!'
            else: return _car[0]

class UpdateMixin(Mixin):
    def update_car(self):
        data = super().get_data()
        flag = False
        try:
            id = int(input('Введите id машины: '))

        except ValueError:
            print('Введите корректное id!')
            return self.update_car()
        else: 
            one_car = list(filter(lambda x: x['id'] == id, data))
            if not one_car: return 'Такого продукта нет!'
            car = data.index(one_car[0])
            choice = int(input('Что бы вы хотели изменить? (1 - Марка, 2 - Модель, 3 - Год выпуска, 4 - Объем двигателя, 5 - Цвет, 6 - Тип кузова, 7 - Пробег, 8 - Цена):'))
            if choice == 1: 
                data[car]['brand'] = input('Введите новую марку машины: ')
                flag = True
            elif choice == 2:
                data[car]['model'] = input('Введите новую модель машины: ')
                flag = True
            elif choice == 3:
                data[car]['year_of_issue'] = int(input('Введите новый год выпуска машины: '))
                flag = True
            elif choice == 4:
                data[car]['engine_volume'] = input('Введите новый объем двигателя: ')
                flag = True
            elif choice == 5:
                data[car]['color'] = input('Введите новый цвет машины: ')
                flag = True
            elif choice == 6:
                data[car]['body_type'] = input('Введите новый тип кузова машины (седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап): ')
                flag = True
            elif choice == 7:
                data[car]['mileage'] = int(input('Введите новый пробег машины: '))
                flag = True
            elif choice == 8:
                data[car]['price'] = round(float(input('Введите новую цену машины: ')),2)
                flag = True
            else:
                print('Такого поля нет!')
            with open(FILE,'w') as file:
                json.dump(data, file)
        if flag: 
            return 'УСПЕШНО ОБНОВЛЕНО!'
        else: 
            return 'Нет такой машины!'
class DeleteMixin(Mixin):
    def delete_car(self):
        data = super().get_data()
        try:
            id = int(input('Введите id машины: '))
        except ValueError:
            print('Введите корректное id!')
            return self.delete_car()
        else:
            one_car = list(filter(lambda x: x['id'] == id, data))
        if not one_car: 
            return 'Такой машины нет!'
        car = data.index(one_car[0])
        data.pop(car)
        
        
        with open(FILE,'w') as file:
            json.dump(data, file)
        return 'УСПЕШНО УДАЛЕНО!'