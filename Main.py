from Cards import Cards


class Main(Cards):
    cards = Cards()
    command = ""
    func = {'добавить': cards.create_cards, 'сохранить': cards.save_to_csv,
            'читать': cards.read_cards, 'редактировать': cards.edit_card, 'удалить': cards.delete_card}
    while True:
        print("\nВведите команду: добавить, сохранить, читать, редактировать, удалить. "
              "Для выхода введите ""выход""")
        command = input()
        if command == "выход":
            break
        else:
            func[command]()
