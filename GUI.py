__version__ = '1.0'
__author__ = 'Patryk Bajgot'


from Engine import HexClac
from tkinter import Tk, END, Label, Entry, Frame


class MainWindow:

    __height = 150
    __width = 240
    __geometry = str(__width) + "x" + str(__height)
    __title = "Hex Calc"
    __dec_label_name = "Decimal:"
    __hex_label_name = "Hexadecimal:"
    __str_incorrect_data = "Incorrect data"
    __entry_width = 33

    def __init__(self):
        self.__calculate = HexClac()

    def main_window(self):
        """
        Renders an GUI.
        :return: Nothing
        """
        window = Tk()
        window.title(self.__title)
        window.geometry(self.__geometry)
        window.minsize(self.__width, self.__height)
        window.maxsize(self.__width, self.__height)

        def convert_to_hex(key):
            """
            Converts dec into hex and fills entry fields.
            :param key: bind event
            :return: Nothing
            """
            dec_value = dec_input.get()
            if len(dec_value) > 0:
                dec_value = self.__convert(True, dec_value)
            hex_input.delete(0, END)
            hex_input.insert(0, dec_value)

        def convert_to_dec(key):
            """
            Converts hec into dex and fills entry fields.
            :param key: bind event
            :return: Nothing
            """
            hex_value = hex_input.get()
            if len(hex_value) > 0:
                hex_value = self.__convert(False, hex_value)
            dec_input.delete(0, END)
            dec_input.insert(0, hex_value)

        """
        W/A - pack w drugiej lini nie działa poprawnie
        """
        main_frame = Frame(window).pack()
        #main_frame.pack()

        dec_label = Label(main_frame, text=self.__dec_label_name)
        dec_label.place(x=10, y=10)

        dec_input = Entry(main_frame, width=self.__entry_width)
        dec_input.place(x=10, y=30)
        dec_input.bind('<KeyRelease>', convert_to_hex)

        hex_label = Label(main_frame, text=self.__hex_label_name)
        hex_label.place(x=10, y=60)

        hex_input = Entry(main_frame, width=self.__entry_width)
        hex_input.place(x=10, y=80)
        hex_input.bind('<KeyRelease>', convert_to_dec)

        window.mainloop()

    def __convert(self, decimal_bool: bool, value):
        """
        Calls Engine func to convert values.
        :param decimal_bool: boolean to change convert method
        :param value: given value
        :return: converted value
        """
        result = value
        try:
            result = self.__calculate.convert_to_hex(int(result)) \
                if decimal_bool \
                else self.__calculate.convert_to_dec(result)
        except:
            result = self.__str_incorrect_data
        return result
