from Stack import Stack
from random import choice
from copy import deepcopy


class Taquin2:

    PATH = Stack()
    ABANDON = False

    def __init__(self, size):
        self.__size = size
        self.__empty_square = size ** 2
        frame = [i for i in range(1, size**2+1)]
        self.__frame = frame
        self.__original_frame = self.__frame  # pour garder en mémoire le frame original en cas d'abandon, pour montrer
        # au joueur ayant abandonné quelle pouvait être la résolution du taquin.
        self.__to_print = len(str(size // 100))

    def is_valid_move(self, move):
        new_taq = self.MOVES[move](self)
        return new_taq != self.__frame

    def get_frame(self):
        return self.__frame

    def up(self):
        index_empty_square = self.index_empty_square()
        if index_empty_square - self.__size < 0:
            return self.__frame
        else:
            new_frame = deepcopy(self.__frame)
            new_frame[index_empty_square], new_frame[index_empty_square - self.__size] = \
                new_frame[index_empty_square - self.__size], new_frame[index_empty_square]
            return new_frame

    def down(self):
        index_empty_square = self.index_empty_square()
        if index_empty_square + self.__size > self.__empty_square - 1:
            return self.__frame
        else:
            new_frame = deepcopy(self.__frame)
            new_frame[index_empty_square], new_frame[index_empty_square + self.__size] = \
                new_frame[index_empty_square + self.__size], new_frame[index_empty_square]
            return new_frame

    def right(self):
        index_empty_square = self.index_empty_square()
        if (index_empty_square + 1) % self.__size == 0:
            return self.__frame
        else:
            new_frame = deepcopy(self.__frame)
            new_frame[index_empty_square], new_frame[index_empty_square + 1] = \
                new_frame[index_empty_square + 1], new_frame[index_empty_square]
            return new_frame

    def left(self):
        index_empty_square = self.index_empty_square()
        if (index_empty_square - 1) % self.__size - 1 == 0:
            return self.__frame
        else:
            new_frame = deepcopy(self.__frame)
            new_frame[index_empty_square], new_frame[index_empty_square - 1] = \
                new_frame[index_empty_square - 1], new_frame[index_empty_square]
            return new_frame

    def get_size(self):
        return self.__size

    def index_empty_square(self):
        return self.__frame.index(self.__empty_square)

    def set_frame(self, frame_taquin):
        self.__frame = frame_taquin

    def set_original_frame(self, frame_taquin):
        self.__original_frame = frame_taquin

    def is_solved(self):
        return self.__frame == [i for i in range(1, self.__empty_square + 1)]

    def solve_abandoned_taquin(self):
        print("This is how the taquin could have been solved, from the configuration in which it was before you played"
              " your first move :\n")
        print("Original frame of the taquin you tried to solve :\n")
        print(self.__original_frame, "\n")
        self.__frame = self.__original_frame
        solution_moves = ""
        while not self.PATH.is_empty():
            print(self)
            move = self.PATH.pop()
            solution_moves += move
            self.__frame = self.MOVES2[move](self)
        print(self)
        print("This was a way to solve the taquin you were offered to complete.")
        print("Here is the list of the moves to play to achieve this taquin according to the solution which has just"
              " been displayed :")
        print(solution_moves)

    def __str__(self):
        line = ("+----" + "-" * self.__to_print) * self.__size + "+"
        taq_to_print = ""
        i = self.__size
        while i <= self.__size ** 2:
            taq_to_print += line
            line_game = ""
            for j in range(self.__size):
                if self.__frame[i - self.__size:i][j] == self.__size ** 2:
                    nb = "|" + " " * (self.__to_print + 4)
                else:
                    nb = "|" + str(self.__frame[i - self.__size:i][j]).center(self.__to_print + 4)
                line_game += nb
            line_game += "|"
            taq_to_print += "\n" + line_game + "\n"
            i += self.__size
        taq_to_print += line
        taq_to_print += "\n"
        return taq_to_print

    def read_move(self):
        list_coups = list(self.MOVES.keys())
        if "A" in list_coups:
            return "A"
        else:
            coup = choice(list_coups)
        return coup

    @staticmethod
    def create_taquin(size):
        taquin = Taquin2(size)
        shuffle_frame(taquin)
        return taquin, taquin.PATH

    MOVES = {'U': up, 'D': down, 'L': left, 'R': right}
    MOVES2 = {'U': down, 'D': up, 'L': right, 'R': left}  # Ici on inverse pour avoir la bonne combinaison quand on
    # dépile.


def abandon(taquin):
    taquin.MOVES["A"] = Taquin2.solve_abandoned_taquin
    taquin.ABANDON = True


def shuffle_frame(taquin):
    for i in range(taquin.get_size() ** 2 + 1):
        move = taquin.read_move()
        if taquin.is_valid_move(move):
            taquin.PATH.push(move)
            taquin.set_frame(taquin.MOVES[move](taquin))
    taquin.set_original_frame(deepcopy(taquin.get_frame()))


def play_taquin2(size):
    taq, winning_structure = Taquin2.create_taquin(size)
    print(taq)
    i = 0
    while not taq.is_solved():
        if i > 1000:
            print("Attempt to solve the taquin failed... Try again.")
            break
        else:
            i += 1
            if i == 100:
                abandon(taq)
            move = taq.read_move()
            taq.set_frame(taq.MOVES[move](taq))
            if not taq.ABANDON:
                print(taq)
            else:
                break

    if i <= 1000 and not taq.ABANDON:
        print("Turn number {}".format(str(i)))
        print("Puzzled solved, bitch !")



