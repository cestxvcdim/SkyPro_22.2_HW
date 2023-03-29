# SkyPro

## 22.2 Homework

[Repository of my friend](https://github.com/PulserCoder/Homework21.2)

***
About project
***

* Refactor bad code
* Code review

***
Я решил взять работу моего одногруппника, и в ней я нашёл примеры плохого кода:

- `../storage.py`

2 класса написаны в одном файле, я бы вынес каждый класс в отдельный файл.

- `../main.py`

Большая функция `main()`, я бы разделил её на несколько частей:

`main_functions.py`
```python
def create_shop(items, capacity=20):
    return Shop(items, capacity)


def create_store(items, capacity=100):
    return Store(items, capacity)


def print_info(store, shop):
    print("Сейчас хранится:")
    print("В складе хранится:")
    print(store.get_items())
    print("В магазине хранится:")
    print(shop.get_items())
    
    
def is_valid():
    try:
        request = Request(input("Введите запрос: "))
    except IndexError:
        print("Ошибка запроса")
        return False
    return request


def is_enough():
    try:
        count = int(request.amount)
    except ValueError:
        print("Вы не ввели количество продукта, попробуйте снова")
        return False
    return count


def is_place(req):
    if req.from_place.lower() != "склад":
        print("Вы не ввели откуда доставить товар, попробуйте снова")
    if req.to_place.lower() != "магазин":
        print("Вы не ввели куда доставить товар, попробуйте снова")

        
def remove_item():
    try:
        store.remove(request.product, count)
    except Exception:
        print("Такого продукта на складе нет!")
        return False


def add_item():
    try:
        shop.add(count, request.product)
    except Exception:
        print("Недостаточно места в магазине.")
        return False


def main_loop(store, shop):
        while True:
            if not is_valid():
                continue
            request = is_valid()
            if not is_enough():
                continue
            is_place(request)
            if not remove_item():
                continue
            if not add_item():
                continue
            print_info(store, shop)
```

`main.py`

```python
from main_functions import *

def main():
    shop = create_shop(items={
        "яблочки": 3,
        "чипсики": 5,
        "помидорчики": 3
    })
    store = create_store(items={
        "печеньки": 5,
        "бананы": 5,
        "груши": 5
    })
    print_info(store, shop)
    main_loop(store, shop)


if __name__ == "__main__":
    main()
```

Больше примеров плохого кода я не нашёл, Павел проделал отличную работу.
***
