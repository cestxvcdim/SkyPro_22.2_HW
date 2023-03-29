# В задании представлена одна большая функция...
# Делает она всего ничего:
# - читает из строки (файла) `_read`
# - сортирует прочитанные значения `_sort`
# - фильтрует итоговый результат `_filter`

# Конечно, вы можете попробовать разобраться как она
# это делает, но мы бы советовали разнести функционал
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(file):
    return [x.split(';') for x in file.split('\n')]

def _sort(data: list):
    data.sort(key=lambda x: x["age"])
    return data

def _filter(data):
    return [person for person in data if person["age"] >= 10]

def get_users_list():
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


if __name__ == '__main__':
    print(get_users_list())
