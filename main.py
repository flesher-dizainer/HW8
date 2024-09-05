from dataset.marvel import full_dict
from typing import Dict, Any
from pprint import pprint


def str_to_int_or_none(input_value: str) -> (int | None):
    """
    Конвернтер строки в число
    :param input_value: строка
    :return: число или None
    """
    if input_value.isdigit():
        return int(input_value)
    else:
        return None


def user_input_id() -> list[int | None]:
    """
    Функция запроса чисел у пользователя
    :return: список чисел и None
    """
    return list(map(str_to_int_or_none, input('Введите цифры через пробел: ').split()))


def int_to_str_dict_year(**marvel_dict):
    """
    Конвертер числа в строку
    :param marvel_dict: словарь
    :return: новый словарь со строкой ключа year
    """
    marvel_dict['year'] = str(marvel_dict['year'])
    return marvel_dict


def print_result(print_data, description):
    print('=' * 50)
    print(description)
    print('=' * 50)
    pprint(print_data, indent=4, sort_dicts=False)
    print('=' * 50)
    print()


def main():
    description = 'Задание: Используйте `filter`, чтобы создать словарь, содержащий исходные `id` и другие ключи, но только для тех фильмов, `id` которых присутствуют в списке, полученном на предыдущем шаге.'
    list_user_id = user_input_id()
    list_dict_filter_marvel = dict(filter(lambda x: x[0] in list_user_id, full_dict.items()))
    print_result(list_dict_filter_marvel, description)

    description = 'Задание: Создайте множество с помощью `set comprehension`, собрав уникальные значения ключа `director` из словаря.'
    set_director = set(value['director'] for key, value in full_dict.items())
    print_result(set_director, description)

    description = 'Задание: С помощью `dict comprehension` создайте копию исходного словаря `full_dict`, преобразовав каждое значение [year] в строку.'
    copy_full_dict = {key: int_to_str_dict_year(**value) for key, value in full_dict.items()}
    print_result(copy_full_dict, description)

    description = 'Задание: Используйте `filter`, чтобы получить словарь, содержащий только те фильмы, которые начинаются на букву `Ч`.'
    marvel_filter_title_ch = dict(filter(lambda x: x[1]['title'][0].strip().lower() == 'ч',
                                         filter(lambda x: x[1]['title'] is not None, full_dict.items())
                                         ))
    print_result(marvel_filter_title_ch, description)

    description = (
        'Задание: **Опционально:** Отсортируйте словарь `full_dict` по одному параметру с использованием `lambda`,'
        'создавая аналогичный по структуре словарь.'
        'Обязательно укажите, по какому параметру вы производите сортировку.')
    items_list = dict(sorted(full_dict.items(), key=lambda x: x[1]['year'] if isinstance(x[1]['year'], int) else False))
    print_result(items_list, description)

    description = (
        'Задание: **Опционально:** Отсортируйте словарь `full_dict` по двум параметрам с использованием `lambda`,'
        ' создавая аналогичный по структуре словарь.'
        ' Обязательно укажите, по каким параметрам вы производите сортировку.')
    # сперва создаём словарь без None, потом сортируем по 2 ключам, по году и названию
    filter_full_dict = dict(sorted(
        (item for item in full_dict.items() if isinstance(item[1]['year'], int) & isinstance(item[1]['title'], str)),
        key=lambda item: (item[1]['year'], item[1]['title'])
    ))
    print_result(filter_full_dict, description)


if __name__ == '__main__':
    main()
