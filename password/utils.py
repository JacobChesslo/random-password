def to_bool(boolean: bool):
    """
    Checks if an argument is of type bool:
        - If argument is type bool, simply returns argument
        - If argunent is type str, attempts to convert to type bool
        - Raises TypeError otherwise

    :param boolean: bool, str
        argument to be converted to type bool
    :return: bool
        original argument or converted string-to-bool argument
    """
    if isinstance(boolean, bool):
        return boolean

    if not isinstance(boolean, str):
        raise TypeError('value {} is not a bool'.format(boolean))

    if boolean.lower() == 'true':
        return True
    elif boolean.lower() == 'false':
        return False
    else:
        raise TypeError('value {} is not a bool'.format(boolean))


def to_int(value: int):
    """
    Checks if an argument is of type int:
        - If argument is of type int, simply returns argument
        - If argument is of type float, if it's int representation is the
            same as the float representation, returns int(float)
        - If argument is of type str, if it can be converted to type float,
            recursively calls function with float(str)
        - Raises TypeError otherwise

    :param value: int, float, str
        argument to be converted to type int
    :return: int
        original argument if type int, otherwise converted string-to-int or float-to-int argument
    """
    if isinstance(value, int):
        return value

    if isinstance(value, float):
        if int(value) == value:
            return int(value)
        else:
            raise TypeError('value {} is not an int'.format(value))
    elif isinstance(value, (list, set, tuple)):
        if len(value) == 1:
            return to_int(value[0])
        else:
            raise TypeError('value {} is not an int'.format(value))
    elif isinstance(value, str):
        try:
            value = float(value)
            return to_int(float(value))
        except (TypeError, ValueError):
            raise TypeError('value {} is not an int'.format(value))
    else:
        raise TypeError('value {} is not an int'.format(value))
