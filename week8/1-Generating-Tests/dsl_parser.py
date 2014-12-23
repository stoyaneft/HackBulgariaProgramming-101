def is_empty_line(line):
    return len(line.strip()) == 0


def lines(textContents):
    return textContents.split("\n")


def unlines(lineData):
    return "\n".join(lineData)


def parse_description(line):
    return """{}""".format(line)


def parsed_test_case(test_case):
    splitted_case = test_case.split('->')
    comment = splitted_case[0].strip()
    expression = splitted_case[1].strip()
    expression_left = expression.split('==')[0].strip()
    expression_right = expression.split('==')[1].strip()
    if expression_right == 'True' or expression_right == 'False':
        return 'self.assert{}({}, {})'.format(
            str(expression_right), expression_left, comment)
    else:
        return 'self.assertEqual({}, {})'.format(
            expression_right, expression_left, comment)
