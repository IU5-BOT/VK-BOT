# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import re


def main():
    pattern = re.compile(r'((н+(е|e)+т*)|(n+o+))*\s*,*\s*((т+ы+)|(y+o+u+))')
    if pattern.match('you'):
        print('блииин')


if __name__ == '__main__':
    main()
