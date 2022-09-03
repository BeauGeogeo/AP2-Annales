class ListError(Exception):
    pass


class List:

    def __init__(self, *args):
        """
        :param args:
        :type args: tuple
        :build: a new empty list if args is empty,
                or a list whose head is first element of args,
                and tail list is second element of args.
        :UC: len(args) in {0, 2}
             and if len(args) == 2, is_instance(args[1], List)
        """
        if len(args) == 0:
            self.__content = dict()
        elif len(args) == 2:
            if isinstance(args[1], List):
                self.__content = {'head': args[0],
                                  'tail': args[1]}
            else:
                raise ListError('bad type for second argument')
        else:
            raise ListError('bad number of arguments')

    def is_empty(self):
        """
        :return:
           - True if self is empty
           - False otherwise
        :rtype: bool
        :UC: none
        """
        return len(self.__content) == 0

    def head(self):
        """
        :return: head element of self
        :raise: :class:`ListError` if self is empty
        """
        try:
            return self.__content['head']
        except KeyError:
            raise ListError('head: empty list')

    def tail(self):
        """
        :return: tail list of self
        :raise: :class:`ListError` if self is empty
        """
        try:
            return self.__content['tail']
        except KeyError:
            raise ListError('tail: empty list')

    def __len__(self):
        """
        :return: length of self
        :rtype: int
        :UC: none
        """
        if self.is_empty():
            return 0
        else:
            return 1 + self.tail().__len__()

    def __str__(self):
        """
        :return: a string representation of list self
        :rtype: str
        :UC: none
        """

        def str_content(self, item_number=0):
            if self.is_empty():
                return ''
            elif item_number == 50:
                return ', ...'
            else:
                comma = '' if item_number == 0 else ', '
                return (comma + str(self.head()) +
                        str_content(self.tail(), item_number + 1))

        return '[{:s}]'.format(str_content(self))

    def set_head(self, x):
        """
        :param x:
        :type x: any
        :return: None
        :side effect: replace head element of self with x.
        :UC: self must be non empty
        :raise: :class:`ListError` if self is empty
        """
        try:
            self.__content['head'] = x
        except KeyError:
            raise ListError('set_head: empty list')

    def set_tail(self, l):
        """
        :param l:
        :type l: List
        :return: None
        :side effect: replace head element of self with x.
        :UC: self must be non empty
        :raise: :class:`ListError` if self is empty or if l is not a List
        """
        if isinstance(l, List):
            try:
                self.__content['tail'] = l
            except KeyError:
                raise ListError('set_tail: empty list')
        else:
            raise ListError('set_tail: argument is not a list')


def list2nativ(l2native):
    if l2native.is_empty():
        return []
    else:
        return [l2native.head()] + list2nativ(l2native.tail())


def native2list(native2l):
    if len(native2l) == 0:
        return List()
    else:
        return List(native2l[0], native2list(native2l[1:]))  # Demander pourquoi PyCharm me met "Expected type tuple,
    # got List instead alors que quand je mets le tout dans un tuple, la fonction ne marche pas et j'ai ListError("Bad
    # number of arguments")


