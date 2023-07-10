import random
import sys


class RandomPassword:
    PASSWORD_LENGTH: int = 15
    ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'
    NUMBERS = '1234567890'
    SPECIALS = '+_-=\\/?<>.,!@#$%^&*()\':;\"~'

    def __init__(self):
        print(
            "______             _____\n" +
            "| ___ \\           |  __ \\\n" +
            "| |_/ /_ _ ___ ___| |  \\/ ___ _ __\n" +
            "|  __/ _` / __/ __| | __ / _ \\ '_ \\\n" +
            "| | | (_| \\__ \\__ \\ |_\\ \\  __/ | | |\n" +
            "\\_|  \\__,_|___/___/\\____/\\___|_| |_|"
        )

        self.__run(without_asks='--no-asks' in sys.argv)

    def __run(self, without_asks: bool = False):
        if without_asks:
            length = self.PASSWORD_LENGTH
            complexity = self.ALPHABETS + self.ALPHABETS.upper() + self.NUMBERS + self.SPECIALS
        else:
            length = self.__ask_password_length()
            complexity = self.__ask_complexity_password()

        generated_pass = "".join(random.sample(complexity, length))

        print('=' * 40)
        print("Password Length: %s" % length)
        print("New Password: %s" % generated_pass)
        print('=' * 40)

    def __ask_password_length(self) -> int:
        print('=' * 40)
        input_length = input(
            "How many symbols must have your password? (Default length \033[1m%d\033[0m symbols): "
            % self.PASSWORD_LENGTH
        ) or str(self.PASSWORD_LENGTH)

        if not input_length.isdigit():
            raise RuntimeError('Length value is not decimal!')

        input_length = int(input_length)

        return self.PASSWORD_LENGTH if input_length <= 0 else input_length

    def __ask_complexity_password(self) -> str:
        complexity = self.ALPHABETS

        if (input('Add uppercase letter? [Y/n]') or 'Y') in ['Y', 'y']:
            complexity += self.ALPHABETS.upper()

        if (input('Add numbers? [Y/n]') or 'Y') in ['Y', 'y']:
            complexity += self.NUMBERS

        if (input('Add special chars? [Y/n]') or 'Y') in ['Y', 'y']:
            complexity += self.SPECIALS

        return complexity


try:
    RandomPassword()
except RuntimeError as message:
    print("\033[91m%s\033[0m" % message)
