#coding: utf-8

#######################################################################
#            Monitoria de matemática discreta 2016.2                  #
#                  Monitora: Ivyna Alves                              #
#                  Prof.: Leandro Balby Marinho                       #
#                                                                     #
#	Primeira atividade de programção + matemática discreta (extra)    #
#	Objetivo: trabalhar recursão e custo com algoritmos de busca e    #
#	ordenação(busca binária e quick sort).                            #
#                                                                     #
#	Nota está dividida: 30% --> testes e 70% --> design de código     #
#######################################################################

'''
    Algorithm binary search index with recursion
    :return: index of value in collection
'''
def buscaBinariaIndice(lista, valor):
    return buscaBinaria(lista, valor, 0, len(lista)-1)

def buscaBinaria(lista, valor, left, right):
    mid = int((left + right) / 2)  # floor

    if valor in lista:
        if lista[mid] == valor:
            return mid

        elif lista[mid] < valor:
            return buscaBinaria(lista, valor, mid + 1, right)

        else:
            return buscaBinaria(lista, valor, left, mid - 1)

    else:
        return -1

'''
    Recursive sorting algorithm with limits in collection
'''
def quickSort(lista, inicio, fim):
    if len(lista) <= 0:
        return
    if inicio < 0 or fim <= 0:
        return
    if fim > len(lista) - 1:
        return

    if (inicio < fim):
        pivot = particion(lista, inicio, fim)
        quickSort(lista, inicio, pivot - 1)
        quickSort(lista, pivot + 1, fim)


def particion(lista, inicio, fim):
    pivot = lista[inicio]

    left = inicio + 1
    right = fim

    while left <= right:
        if lista[left] <= pivot:
            left += 1

        elif pivot < lista[right]:
            right -= 1

        else:
            troca(lista, left, right)
            left += 1
            right -= 1

    lista[inicio] = lista[right]
    lista[right] = pivot
    return pivot

'''
    Auxiliar algorithm to do swaps in elements of collection
'''
def troca(lista, i, j):
    swap = lista[i]
    lista[i] = lista[j]
    lista[j] = swap
