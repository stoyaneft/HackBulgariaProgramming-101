def parse_choices(filename):
    with open(filename, 'r') as choices_file:
        content = choices_file.read()
        team_choices = [choice.split(' ') for choice in content.split('\n')]
        return team_choices


def main():
    print(parse_choices('choices.csv'))

if __name__ == '__main__':
    main()
