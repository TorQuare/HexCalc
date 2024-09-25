__version__ = '1.0'
__author__ = 'Patryk Bajgot'


class HexClac:

    def __init__(self):
        self.__hex_font = '\u001b[1;32;40m'
        self.__nor_font = '\u001b[0;37;40m'

    @staticmethod
    def convert_to_hex(input_dec: int):
        """
        Converts value into hex.
        :param int input_dec: given dec value
        :return: Hex value
        """
        return hex(input_dec)

    @staticmethod
    def convert_to_dec(input_hex):
        """
        Converts value into dec.
        :param input_hex: given hex value
        :return: Dec value
        """
        return int(input_hex, 16)

    def calculate(self):
        """
        Startup func. Converts dec into hex.
        :return: Nothing
        """
        while(True):
            print(self.__nor_font + 'Decimal: ')
            input_dec = input()
            if type(input_dec) is not int:
                continue
            print(self.__hex_font + self.convert_to_hex(int(input_dec)))
