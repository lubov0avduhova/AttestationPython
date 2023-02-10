import csv
from datetime import datetime
from CardInfo import CardInfo


class Cards(CardInfo):
    listcards = []
    value = 0

    def read_cards(self):

        for i in self.listcards:
            print("\nПорядковый номер " + str(self.listcards.index(i)))
            print("Информация заметки:")
            for j in i:
                print(str(j))

    def create_cards(self):
        new_card = CardInfo()
        new_card.set_date(datetime.now())
        print("Введите заголовок:")
        new_card.set_header(input())
        print("Введите тело заметки: ")
        new_card.set_note_body(input())

        list = []
        list.append(new_card.get_date())
        list.append(new_card.get_header())
        list.append(new_card.get_note_body())

        self.listcards.append(list)
        print("Заметка успешно сохранена. Порядковый номер: " + str(self.value))
        self.value += 1

    def delete_card(self):
        print("Введите порядковый номер заметки")
        del self.listcards[int(input())]
        print("Заметка успешно удалена")

    def edit_card(self):
        print("Напишите порядковый номер карточки и вы хотите изменить : ""заголовок"", ""тело""\n"
              "пример: 1 заголовок")
        edit_number, edit_card = input().split(' ')
        print("Введите новую информацию:")
        while True:
            if edit_card.lower() == "заголовок":
                self.listcards[int(edit_number)][1] = input()
                break
            elif edit_card.lower() == "тело":
                self.listcards[int(edit_number)][2] = input()
                break
            else:
                print("Ошибка. Введите еще раз команду")

    def save_to_csv(self):
        with open('cards_csv.csv', 'w') as f:
            write = csv.writer(f)
            write.writerows(self.listcards)
            print("Сохранено в файл")
