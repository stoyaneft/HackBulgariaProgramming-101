from dsl_parser import *


class DSLTestsGenerator:

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.dsl_lines = lines(file.read())
        self.filename = filename
        self.imports = []
        self.test_description = ''
        self.test_cases = []

    def _parse_dsl(self):
        test_cases_started = False
        for line in self.dsl_lines:
            if not test_cases_started:
                if is_empty_line(line):
                    test_cases_started = True
                elif line[0] == '"':
                    self.test_description = parse_description(line)
                else:
                    self.imports.append(line)
            else:
                if not is_empty_line(line):
                    self.test_cases.append(parsed_test_case(line))

    def create_test_file(self):
        self._parse_dsl()
        name = self.filename.split('.')[0]
        words = [x.capitalize() for x in name.split('_')]
        class_name = ''.join(words)

        imports_string = unlines(self.imports)
        TAB = '    '
        with open(name + '.py', 'w') as test_file:
            test_file.write('import unittest\n\n')
            test_file.write(imports_string)
            test_file.write('\n\n\n')
            test_file.write(
                'class {}(unittest.TestCase):\n'.format(class_name))
            if self.test_description:
                test_file.write(TAB + self.test_description + '\n')
            for i, test_case in enumerate(self.test_cases):
                test_file.write(
                    '\n' + TAB + 'def TestCase{}(self):\n'.format(i + 1))
                test_file.write(TAB + TAB + test_case + '\n')
            if not self.test_cases:
                test_file.write(TAB + 'pass\n')
            test_file.write(
                '\n\nif __name__ == "__main__":\n{}unittest.main()\n'.format(
                    TAB))


if __name__ == '__main__':
    test_gen = DSLTestsGenerator("is_prime_test.dsl")
    test_gen.create_test_file()
    print(test_gen.imports, test_gen.test_description, test_gen.test_cases)
