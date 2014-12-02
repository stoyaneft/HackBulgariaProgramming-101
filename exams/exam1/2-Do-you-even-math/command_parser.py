class CommandParser():

    def __init__(self):
        self.__commands = {}

    def add_command(self, command, function):
        self.__commands[command] = function

    def execute(self, input):
        input = input.split(" ")
        command = input[0]
        arguments = input[1:]
        try:
            self.__commands[command](*arguments)
        except KeyError:
            print('No such command!')
