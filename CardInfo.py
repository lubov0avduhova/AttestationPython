class CardInfo:
    __date = ""
    __header = ""
    __note_body = ""

    def get_card_info(self):
        return str(self.__date) + "\n" + self.__header + "\n" + self.__note_body

    def get_date(self):
        return self.__date

    def get_header(self):
        return self.__header

    def get_note_body(self):
        return self.__note_body

    def set_header(self, header):
        self.__header = header

    def set_note_body(self, note_body):
        self.__note_body = note_body

    def set_date(self, date):
        self.__date = date
