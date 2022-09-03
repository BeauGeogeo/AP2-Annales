class StackEmptyError(Exception):
    """
    Exception for empty stacks
    """

    def __init__(self, msg):
        self.message = msg


class Stack:

    def __init__(self):
        """
        :build: a new empty stack
        :UC: none
        """
        self.__content = []

    def top(self):
        """
        :return: element on top of self without removing it
        :UC: self must be non empty
        """
        try:
            return self.__content[-1]
        except IndexError:
            raise StackEmptyError('empty stack, nothing on the top')

    def push(self, x):
        """
        :param x: a value
        :type x: any
        :return: None
        :rtype: Nonetype
        :Side effect: stack self contains a new value : x
        :UC: none
        """
        self.__content.append(x)

    def pop(self):
        """
        :return: element on top of self
        :Side effect: self contains an element less
        :UC: self must be non empty
        """
        try:
            return self.__content.pop()
        except IndexError:
            raise StackEmptyError('empty stack, nothing to pop')

    def is_empty(self):
        """
        :return:
           * ``True`` if s is empty
           * ``False`` otherwise
        :rtype: bool
        :UC: none
        """
        return self.__content == []


def stack_size(st):
    st2 = Stack()
    res = 0
    while not st.is_empty():
        st2.push(st.pop())
        res += 1
    while not st2.is_empty():
        st.push(st2.pop())
    return res


def pile2native(p2native):
    if p2native.is_empty():
        return []
    else:
        elt_pop = p2native.pop()
        return pile2native(p2native) + [elt_pop]


def native2pile(native2p):  # à tester. Peut-être échanger l'ordre dans le else
    if len(native2p) == 0:
        return Stack()
    else:
        p = Stack()
        p.push(native2p)
        return native2pile(native2p)
