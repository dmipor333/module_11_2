'''Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента
 и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип'''
import inspect
def introspection_info(obj):
    obj_type = type(obj)
    obj_attributes = dir(obj)

    def get_methods():
        return get_methods.__dir__()

    module = obj.__class__.__module__


    dictionary = {'type': obj_type, 'attributes': obj_attributes, 'methods': get_methods(), 'module': module}
    return dictionary


number_info = introspection_info(42)
print(number_info)