import random


class RandomPassword:
    __password_length: int = 15
    __alphabets = 'abcdefghijklmnopqrstuvwxyz'
    __numbers = '1234567890'
    __specials = '+_-=\\/?<>.,!@#$%^&*()\':;\"~'

    def __init__(self):
        self.__password_length = self.__ask_password_length()

    def run(self):
        complexity = self.__ask_complexity_password()
        generated_pass = "".join(random.sample(complexity, self.__password_length))

        print("Length: %s" % self.__password_length)
        print("New Password: %s" % generated_pass)

    def __ask_password_length(self) -> int:
        input_length = input(
            "How many symbols must have your password? (Default length \033[1m%d\033[0m symbols): " % self.__password_length)
        if not input_length.isdigit():
            raise RuntimeError('Length value is not decimal!')

        input_length = int(input_length)

        return self.__password_length if input_length <= 0 else input_length

    def __ask_complexity_password(self) -> str:
        complexity = self.__alphabets

        if (input('Add uppercase letter? [Y/n]') or 'Y') == 'Y':
            complexity += self.__alphabets.upper()

        if (input('Add numbers? [Y/n]') or 'Y') == 'Y':
            complexity += self.__numbers

        if (input('Add special chars? [Y/n]') or 'Y') == 'Y':
            complexity += self.__specials

        return complexity


try:
    randomizer = RandomPassword()
    randomizer.run()
except RuntimeError as message:
    print("\033[91m%s\033[0m" % message)
