
class RandomPassword:
    password_length: int = 15

    def __init__(self):
        self.run()

    def run(self):
        input_length = input('How many symbols must have your password? (Default: %d)' % self.password_length)
        print(int(input_length))


RandomPassword()