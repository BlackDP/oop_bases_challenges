"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, desc: str, price: float, weight: float):
        self.name = name
        self.desc = desc
        self.price = price
        self.weight = weight

    def get_product_info(self):
        return f"Информация о продукте: Наименование: {self.name}, Описание: {self.desc}, Цена: {self.price}руб., Вес: {self.weight}кг."

if __name__ == '__main__':
    product1 = Product(
        name='Творог',
        desc='Не вкусный, не покупайте',
        price= 190.5,
        weight= 0.940,
    )
    print(product1.get_product_info())
