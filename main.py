dict_films = dict()

choose = input('Поиск по: \n'
               '1 фильмам; \n'
               '2 актерам. ')
val1, val2 = map(str, input('Введите данные через запятую.').split(', '))

with open('input.txt', 'r', encoding="utf-8") as f:
    a = f.readlines()
    for lines in a:
        line = lines.replace('\n', '').split(': ')
        dict_films[line[0]] = line[1].split(', ')


def print_actors():
    lst1 = []
    lst2 = []
    for i in dict_films.keys():
        if val1 in dict_films[i]:
            lst1.append(i)
        if val2 in dict_films[i]:
            lst2.append(i)
    print('1) ', end='')
    print(*(set(lst1) | set(lst2)), sep=', ')
    print('2) ', end='')
    if len(set(lst1) & set(lst2)) == 0:
        print('Нет общих фильмов')
    else:
        print(*(set(lst1) & set(lst2)), sep=', ')
    if lst1 == lst2:
        print('3) ', end='')
        print('Они снимались в одном фильме.')
    else:
        print('3) ', end='')
        print(*(set(lst1) - set(lst2)), sep=', ')


def print_films():
    art1 = art2 = set()
    if val1 in dict_films:
        art1 = set(dict_films[val1])
    if val2 in dict_films:
        art2 = set(dict_films[val2])
    print('1) ', end='')
    print(*(set(art1) | set(art2)), sep=', ')
    print('2) ', end='')
    if len(set(art1) & set(art2)) == 0:
        print('Нет актеров, снимавшихся в обоих фильмах')
    else:
        print(*(set(art1) & set(art2)), sep=', ')
    print('3) ', end='')
    print(*(art1 - art2), sep=', ')


if choose == '1':
    print_films()
else:
    print_actors()
