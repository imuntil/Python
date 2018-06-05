import unittest


def get_formatted_name(first_name, last_name):
    return '{} {}'.format(first_name.title(), last_name.title())


def get_formatted_name2(first, last, middle=''):
    if middle:
        return '{} {} {}'.format(first, middle, last).title()
    else:
        return '{} {}'.format(first, last).title()


class NamesTestCase(unittest.TestCase):
    """测试get_formatted_name"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('zhin', 'until')
        self.assertEqual(formatted_name, 'Zhin Until')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name2('zhin', 'until', 'd')
        self.assertEqual(formatted_name, 'Zhin D Until')


unittest.main()
