from password.password import Password
from password.utils import to_bool, to_int


def generate_random_password(length: int = 20,
                             numbers: bool = True,
                             lowercase: bool = True,
                             uppercase: bool = True,
                             symbols: bool = True,
                             save_preference: bool = True):
    """
    Function to generate a pseudo-randomly generated password

    :param length: int
        character-length of password, must be greater than 0
        Default: 20
    :param numbers: bool
        Flag whether to include numbers
        Digits 0-9, contained in string.digits
        Default: True
    :param lowercase: bool
        Flag whether to include English lowercase letters
        Letters a-z, contained in string.ascii_lowercase
        Default: True
    :param uppercase: bool
        Flag whether to include uppercase letters
        Letters A-Z, contained in string.ascii_uppercase
        Default: True
    :param symbols: bool
        Flag whether to include symbols
        Symbols contained in string.symbols
        Default: True
    :param save_preference: bool
        Flag whether to save the above preferences in the class object
        Default: True
    :return: str
        Pseudo-randomly generated password
    """

    """
    Verify requirements
    """
    length = to_int(length)
    numbers = to_bool(numbers)
    uppercase = to_bool(uppercase)
    symbols = to_bool(symbols)
    save_preference = to_bool(save_preference)
    if not any(flag is True for flag in (numbers, lowercase, uppercase, symbols)):
        raise ValueError('Must include at least one true flag: numbers, lowercase, uppercase, symbols all False')
    if length < 1:
        raise ValueError('Length {} must be at least 1'.format(length))

    """
    Create object, set password requirements, generate password and returns
    """
    password = Password()
    password.gather_requirements(
        length=length,
        numbers=numbers,
        lowercase=lowercase,
        uppercase=uppercase,
        symbols=symbols,
        save_preference=save_preference
    )

    return password.generate_password()
