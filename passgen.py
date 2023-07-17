import random
import sys

import math
import pyperclip


class RandomPassword:
    PASSWORD_LENGTH: int = 15
    ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'
    NUMBERS = '1234567890'
    SPECIALS = '+_-=\\/?<>.,!@#$%^&*()\':;\"~'

    def __init__(self):
        print(
            "\t______             _____\n" +
            "\t| ___ \\           |  __ \\\n" +
            "\t| |_/ /_ _ ___ ___| |  \\/ ___ _ __\n" +
            "\t|  __/ _` / __/ __| | __ / _ \\ '_ \\\n" +
            "\t| | | (_| \\__ \\__ \\ |_\\ \\  __/ | | |\n" +
            "\t\\_|  \\__,_|___/___/\\____/\\___|_| |_|"
        )

        self.__run(
            without_asks='--no-asks' in sys.argv,
            to_clipboard='--clipboard' in sys.argv
        )

    def __run(self, without_asks: bool = False, to_clipboard: bool = False):
        length = self.PASSWORD_LENGTH if without_asks else self.__ask_password_length()
        complexity = self.__ask_complexity_password(length, without_asks)
        generated_pass = "".join(random.sample(complexity, length))

        self.print_line()
        print("Password Length: %s" % length)
        print("Generated Password: \033[1;33m%s\033[0m" % generated_pass)
        self.print_line()

        self.__ask_copy_to_clipboard(
            generated_password=generated_pass,
            ask=to_clipboard
        )

    def __ask_password_length(self) -> int:
        self.print_line()
        input_length = input(
            "\t\033[0;36mHow many symbols must have your password? " +
            "(Default length \033[1;36m%d\033[0;36m symbols):\033[0m "
            % self.PASSWORD_LENGTH
        ) or str(self.PASSWORD_LENGTH)

        if not input_length.isdigit():
            raise RuntimeError('Length value is not decimal!')

        input_length = int(input_length)

        return self.PASSWORD_LENGTH if input_length <= 0 else input_length

    def __ask_complexity_password(self, length: int, without_asks: bool = False) -> str:
        sections_count: int = 4
        choice: dict = {
            'uppercase': True,
            'numbers': True,
            'specials': True
        }
        asks: dict = {
            'uppercase': '\t\033[0;36mUse uppercase letter? [\033[1;36mY\033[0;36m/n]:\033[0m ',
            'numbers': '\t\033[0;36mUse numbers? [\033[1;36mY\033[0;36m/n]:\033[0m ',
            'specials': '\t\033[0;36mUse special chars? [\033[1;36mY\033[0;36m/n]:\033[0m '
        }

        if not without_asks:
            for complexity_type, question in asks.items():
                if (input(question) or 'Y') not in ['Y', 'y']:
                    sections_count -= 1
                    choice[complexity_type] = False

        length_section: int = math.ceil(length / sections_count)
        complexity = "".join(random.sample(self.ALPHABETS, length_section))

        if choice['uppercase']:
            complexity += "".join(random.sample(self.ALPHABETS.upper(), length_section))

        if choice['numbers']:
            complexity += "".join(random.sample(self.NUMBERS, length_section))

        if choice['specials']:
            complexity += "".join(random.sample(self.SPECIALS, length_section))

        return complexity

    @staticmethod
    def __ask_copy_to_clipboard(generated_password: str, ask: bool = True):
        question: str = '\t\033[0;36mCopy password to clipboard? [y/\033[1;36mN\033[0;36m]:\033[0m '

        if ask or (input(question) or 'N') in ['Y', 'y']:
            pyperclip.copy(generated_password)

    @staticmethod
    def print_line(line_length: int = 60):
        print('=' * line_length)


try:
    RandomPassword()
except RuntimeError as message:
    print("\033[91m%s\033[0m" % message)
