import string
import secrets
import random


class Password(object):
    """
    Password object for the generation of a pseudo-random password
    """

    """
    Class attributes
    """
    length = 20
    numbers = True
    lowercase = True
    uppercase = True
    symbols = True

    def __init__(self):
        """
        Empty init function
        """
        pass

    def gather_requirements(self,
                            length: int = length,
                            numbers: bool = numbers,
                            lowercase: bool = lowercase,
                            uppercase: bool = uppercase,
                            symbols: bool = symbols,
                            save_preference: bool = True
                            ):
        """
        Gathers the requirements of a pseudo-random password, and saves the preference
        of the requirements if flagged

        If none of the requirements are true, raises a ValueError

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
        :return: None
        """
        if not any(flag is True for flag in (numbers, lowercase, uppercase, symbols)):
            raise ValueError('Must include at least one true flag: numbers, lowercase, uppercase, symbols all False')
        if length < 1:
            raise ValueError('Length {} must be at least 1'.format(length))
        if save_preference:
            Password._save_requirements(
                length=length,
                numbers=numbers,
                lowercase=lowercase,
                uppercase=uppercase,
                symbols=symbols
            )

        return

    @classmethod
    def _save_requirements(cls,
                           length: int = 20,
                           numbers: bool = True,
                           lowercase: bool = True,
                           uppercase: bool = True,
                           symbols: bool = True
                           ):
        """
        Sets the class attributes

        :param length: int
            default character-length of password, must be greater than 0
            Default: 20
        :param numbers: bool
            default flag whether to include numbers
            Digits 0-9, contained in string.digits
            Default: True
        :param lowercase: bool
            default flag whether to include English lowercase letters
            Letters a-z, contained in string.ascii_lowercase
            Default: True
        :param uppercase: bool
            default flag whether to include uppercase letters
            Letters A-Z, contained in string.ascii_uppercase
            Default: True
        :param symbols: bool
            default flag whether to include symbols
            Symbols contained in string.symbols
            Default: True
        :return: None
        """
        cls.length = length
        cls.numbers = numbers
        cls.lowercase = lowercase
        cls.uppercase = uppercase
        cls.symbols = symbols

        return

    def generate_password(self):
        """
        Generates password using requirements
        Assumes that method gather_requirements has been called

        :return: str
            pseudo-randomly generated password
        """
        if not all(hasattr(self, variable) for variable in ('length', 'numbers', 'lowercase', 'uppercase', 'symbols')):
            raise AttributeError('password object does not have all required variables')

        # Adds to list of possible characters
        possible_characters = ''
        if self.numbers:
            possible_characters = possible_characters + string.digits
        if self.lowercase:
            possible_characters = possible_characters + string.ascii_lowercase
        if self.uppercase:
            possible_characters = possible_characters + string.ascii_uppercase
        if self.symbols:
            possible_characters = possible_characters + string.punctuation

        # Shuffles possible characters
        possible_characters = ''.join(random.shuffle(list(possible_characters)))

        while True:
            """
            Iterates until 'check' is verified
            """

            """
            This is where the magic happens:
                Fills a length-long list with a pseudo-random choice from the possible characters
                Joins them into a single password
            """
            self.password = ''.join(secrets.choice(possible_characters) for _ in range(self.length))

            """
            This is where verification happens:
                Makes sure all of the flagged conditions are met before breaking out of while loop
                Such that only one instance of the flagged-condition is met in the password if True,
                otherwise ignores that requirement
            """
            if all(
                    [
                        any(character.islower() for character in self.password) if self.lowercase else True,
                        any(character.isupper() for character in self.password) if self.uppercase else True,
                        any(character.isdigit() for character in self.password) if self.numbers else True,
                        any(character in string.punctuation for character in self.password) if self.symbols else True
                    ]
            ):
                break

        return self.password
