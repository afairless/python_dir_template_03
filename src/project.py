#! /usr/bin/env python3

def dummy_function01() -> int:
    """
    This is a function
    """

    return 1


def dummy_function02(input: int) -> int:
    """
    This is a function
    """

    assert input > 0

    return input + 1


def main():

    print('This is the main function.')



if __name__ == '__main__':
    main()
