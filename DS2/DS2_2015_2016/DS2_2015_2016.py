from Liste import *
from Stack import *
from Taquin2 import play_taquin2


p1, p2 = Stack(), Stack()


def initializing_stack(p1, p2):
    p1.push(11)
    p1.push(5)
    p1.push(1)
    p2.push(9)
    p2.push(7)


def initializing_stack_reverse(p1, p2):
    p1.push(1)
    p1.push(5)
    p1.push(11)
    p2.push(7)
    p2.push(9)

# Exo 1


L1 = native2list([1, 3, 5, 7])
L2 = native2list(['Timoleon', 'Calbuth', 'Talon', 'Carmen'])
print(L1, L2)

# Q1


def zipping(l1, l2):  # version récursive
    if l1.is_empty() and l2.is_empty():
        return List()
    else:
        if l1.is_empty():  # bon en fait tout ça pas utile puisque UC : listes de mêmes longueurs
            return l2
        elif l2.is_empty():
            return l1
        else:
            return List((l1.head(), l2.head()), zipping(l1.tail(), l2.tail()))


L = zipping(L1, L2)
print(L)
print(list2nativ(L))
print()

# Q2


def unzipping(l):
    if l.is_empty():
        return l, l
    else:
        l1, l2 = unzipping(l.tail())
        return List(l.head()[0], l1), List(l.head()[1], l2)


l1, l2 = unzipping(L)
print(list2nativ(l1), list2nativ(l2))

# Exercice 2

# Q1


def stack_merge(p1, p2):  # demander si plus rapide ou facile, si forcément récursif
    if p1.is_empty() and p2.is_empty():
        return List()
    elif p1.is_empty():
        return List(p2.pop(), stack_merge(p1, p2))
    elif p2.is_empty():
        return List(p1.pop(), stack_merge(p1, p2))
    else:
        if p1.top() > p2.top():
            return List(p2.pop(), stack_merge(p1, p2))
        else:
            return List(p1.pop(), stack_merge(p1, p2))


initializing_stack(p1, p2)
print("stack_merge1", list2nativ(stack_merge(p1, p2)))

# Q2

# Ma fonction a un effet de bord en ce qu'elle dépile/vide totalement les deux piles p1 et p2 passées en paramètres

# Q3

# Avec des piles cette fois triées dans l'ordre décroissant


def stack_merge2(p1, p2):
    p1_sorted = Stack()
    p2_sorted = Stack()
    while not p1.is_empty():
        p1_sorted.push(p1.pop())
    while not p2.is_empty():
        p2_sorted.push(p2.pop())
    return stack_merge(p1_sorted, p2_sorted)

# On aurait aussi pu tricher en faisant qqch du genre list2nativ, trier la liste python puis nativ2list mais pas sûr
# que ça soit dans les opérations autorisées du DS. Sinon avec fonction qui reverse la liste à la fin comme vue en TD

# On aurait encore pu faire également comme dans le DS de 2018/2019 et produire une stack triée dans l'ordre
# décroissant, et construire la liste en la dépilant.


p1, p2 = Stack(), Stack()
initializing_stack_reverse(p1, p2)
print("stack_merge2", list2nativ(stack_merge2(p1, p2)))


def last(l):
    the_last = l.head()
    if l.tail().is_empty():
        return the_last
    else:
        return last(l.tail())


def length(l):
    cpt = 0
    while not l.is_empty():
        cpt += 1
        l = l.tail()
    return cpt


def rec_length(l):
    if l.is_empty():
        return 0
    else:
        return 1 + rec_length(l.tail())


def nth(l, index):
    if index > length(l) or index < 0:
        raise IndexError
    elif l.is_empty():
        raise ListError('empty list')
    else:
        i = 0
        while i < index:
            l = l.tail()
            i += 1
        return l.head()


def rec_nth(l, index):
    if l.is_empty():
        raise ListError('empty list')
    elif index > length(l)-1 or index < 0:
        raise IndexError
    else:
        if index == 0:
            return l.head()
        else:
            return rec_nth(l.tail(), index-1)


l_index = List(1, List(2, List(3, List())))
print("rec_nth index 0", rec_nth(l_index, 0))
print("rec_nth index 1", rec_nth(l_index, 1))
print("rec_nth index 2", rec_nth(l_index, 2))
# print("rec_nth index 2", rec_nth(l_index, 10))


def concat(l1, l2):
    if l1.is_empty():
        return l2
    else:
        return List(l1.head(), concat(l1.tail(), l2))


def reverse_list(l):
    if l.is_empty():
        return l
    else:
        to_add = List(l.head(), List())
        return concat(reverse_list(l.tail()), to_add)


# Exercice 3

# Q1

# Si on enregistre les mouvements réalisés par la case vide du taquin et qu'on veut les restituer dans l'ordre inverse,
# la structure de pile est particulièrement bien adaptée.
# En effet, on enregistre les déplacements de la case vide lors du mélange. Lorsqu'on dépile, on commence donc par le
# dernier mouvement effectué et on continue ainsi jusqu'au premier effectué, on fait donc le chemin en sens inverse et
# cela remet la case vide dans sa position initiale. Or, dans celle-ci, avant le mélange donc, le taquin est en état
# "résolu" (si on faisait taquin.is_solved() à ce moment là, cela renverrait True)


# Q2


def solve(empty_case_path):
    winning_str = ""
    while not empty_case_path.is_empty():
        winning_str += empty_case_path.pop()  # rien de difficile ici. Comme expliqué dans la question précédente,
        # il suffit de dépiler
    return winning_str


# Q3

# Pour cette question, j'ai modifié, comme suggéré par le sujet d'annale, la classe Taquin en programmant la classe
# Taquin2 à la place, dont on va se servir ici.

# Le plus simple, en relisant ce qui est demandé, est de mettre un input "Voulez-vous abandonner ?" et si la
# réponse est oui alors MOVES devient un dico avec seulement le caractère 'A', donc read_move lit nécessairement ce
# caractère et on arrête la boucle à ce moment, le module Taquin 2 appelant une fonction imprimant toutes les
# instructions

# Mais on peut aussi faire différemment, en prévoyant que la question n'est demandé que toutes les -k itérations, on
# pourrait même rentrer le paramètre du nombre d'itérations après lesquelles on veut se voir proposer l'abandon.

play_taquin2(4)
