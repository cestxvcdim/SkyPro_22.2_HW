from part2.request import Request
from part2.shop import Shop
from part2.storage import Store


def main():
    shop = Shop(items={
        "яблочки": 3,
        "чипсики": 5,
        "помидорчики": 3
    }, capacity=20)

    store = Store(items={
        "печеньки": 5,
        "бананы": 5,
        "груши": 5
    }, capacity=25)
    print("Сейчас хранится:")
    print("В складе хранится:")
    print(store.get_items())
    print("В магазине хранится:")
    print(shop.get_items())
    while True:
        try:
            request = Request(input("Введите запрос: "))
        except IndexError:
            print("Ошибка запроса")
        try:
            count = int(request.amount)
        except ValueError:
            print("Вы не ввели количество продукта, попробуйте снова")
            continue

        if request.from_place.lower() != "склад":
            print("Вы не ввели откуда доставить товар, попробуйте снова")
            continue
        if request.to_place.lower() != "магазин":
            print("Вы не ввели куда доставить товар, попробуйте снова")
            continue
        try:
            store.remove(request.product, count)
        except Exception:
            print("Такого пролдукта на складе нет!")
            continue
        try:
            shop.add(count, request.product)
        except Exception:
            raise
            continue

        print("В складе хранится:")
        print(store.get_items())

        print("В магазине хранится:")
        print(shop.get_items())


if __name__ == "__main__":
    main()
