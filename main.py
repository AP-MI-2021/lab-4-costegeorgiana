from typing import List

import inflect as inflect


def show_menu():
    print("1.Citirea unei liste de float-uri")
    print("2.Afisarea partii intregi a numerelor din lista.")
    print("3.Afisarea numerelor care apartin unui interval deschis.")
    print("4.Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare.")
    print("5.Afisarea listei obtinute prin inlocuirea numerelor cu string-urile lor.")
    print("X.Iesire")


def read_list() -> List[float]:
    lst = []
    lst_str = input("Dati numerele care vor fi incluse in lista separandu-le printr-un spatiu")
    lst_str_split = lst_str.split(' ')
    for numar in lst_str_split:
        lst.append(float(numar))
    return lst


def get_int(lst):
    """
    Inlocuieste numarul real cu partea sa intreaga
    :param lst: lista citita de numere reale
    :return: lista cu formata din parti intregi
    """
    n = len(lst)
    for i in range(n):
        lst[i] = int(lst[i])
    return lst


def print_lst_int(lst):
    lst = get_int(lst)
    print("Lista formata din partea intreaga a numerelor este: ", lst)


def get_numbers(lst) -> List[float]:
    """
    Determina daca elementele din lista initiala fac parte din intervalul deschis si le introduc in lista result.
    :param lst: lista in care se cauta elementele
    :return: lista care contine elementele care indeplinesc conditia
    """
    result = []
    st = input("Dati marginea inferioara a intervalului")
    dr = input("Dati marginea superioara a intervalului")
    for numar in lst:
        if numar > int(st) and numar < int(dr):
            result.append(numar)
    return result


def print_get_numbers(lst):
    result = get_numbers(lst)
    print("Elementele care fac parte din interval sunt: ", result)


def int_div_fract(lst) -> List[float]:
    """
    Determina numerele a caror parte intreaga este divizor a partii fractionare
    :param lst: lista de float-uri
    :return: lista cu elementele care indeplinesc conditia
    """
    result = []
    for numar in lst:
        str_nr = str(numar)
        if "." in str_nr:
            if int(str_nr.split('.')[1]) % int(str_nr.split('.')[0]) == 0 and int(str_nr.split('.')[1]) != 0:
                result.append(numar)
    return result


def print_int_div_fract(lst):
    result = int_div_fract(lst)
    print("Numerele a caror parte intreaga divide partea fractionara sunt: ", result)


def number_to_words(lst) -> List[str]:
    """
    Creeaza o lista formata din lista initiala prin transformarea numerelor in cuvintele respective.
    :param lst: lista initiala de float-uri
    :return: lista obtinuta
    """
    result = []
    p = inflect.engine()
    for numar in lst:
        result.append(p.number_to_words(numar))
    return result


def print_number_to_words(lst):
    result = number_to_words(lst)
    print("Numerele transformate in cuvinte: ", result)


def test_get_int():
    assert get_int([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert get_numbers([6.76, -2.8, 9, 2.3]) == [6, -2, 9, 2]


def test_int_div_fract():
    assert int_div_fract([1.5, -3.3, 8, 9.8, 3.2]) == [1.5, -3.3]


def test_number_to_words():
    assert number_to_words([1.5, -3.3, 8, 9.8, 3.2]) == ["one point five", "minus three point three",
                                                         "eight", "nine point eight", "three point two"]


def main():
    lst = []
    while True:
        show_menu()
        optiune = input("Dati optiunea ")
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print_lst_int(lst)
        elif optiune == '3':
            print_get_numbers(lst)
        elif optiune == '4':
            print_int_div_fract(lst)
        elif optiune == '5':
            print_number_to_words(lst)
        elif optiune == 'X':
            break
        else:
            print("Optiune invalida")


if __name__ == '__main__':
    test_number_to_words()
    test_int_div_fract()
    main()
