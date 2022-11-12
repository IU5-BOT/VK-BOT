# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import re


def main():
    pattern = re.compile(r'(^(((н|h)+(е|e)+т*)|(n+o+)|(н|h(о|o)+у|y))*\s*,*\.*\s*((т+ы+)+|(y|у+o|о+u+)+|u+))[\.,]*$')
    if pattern.match('нет, ты.  '):
        print('EE')


if __name__ == '__main__':
    main()
