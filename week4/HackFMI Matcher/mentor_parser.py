import re


def parse_mentors(filename):
    with open(filename, 'r') as mentors_file:
        mentors_content = mentors_file.read()
    mentor_names_re = re.compile(
        r'### (?P<name>\w+ \w+)')
    mentors = mentor_names_re.findall(mentors_content)
    return mentors


def main():
    print(parse_mentors('mentors.txt'))


if __name__ == '__main__':
    main()
