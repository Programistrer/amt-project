class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print(f"Ваш баланс {self.balance} рублей")

    def deposit(self, amount):
        if amount > 49:
            self.balance = self.balance + amount
            print(f"Вы внесли {amount}. Ваш баланс {self.balance}")
        else:
            print(f"Сумма должна быть от 50 руб")

    def widthraw(self, amount):
        if amount > 50 and amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Вы сняли {amount} руб. Ваш баланс {self.balance}")
        else:
            print(f"Сумма должна быть от 50 руб или недостаточно средств")


class SecureATM(ATM):
    def __init__(self, balance, pin):
        super().__init__(balance)
        self.pin = pin
        self.is_autentificated = False

    def autentificat(self, enter_pin):
        if enter_pin == self.pin:
            self.is_autentificated = True
            print("Аутентификация прошла успешно!")
        else:
            print("Неправильный Pin-code")

    def check_balance(self):
        if self.is_autentificated == True:
            super().check_balance()
        else:
            print("Необходимо пройти аутентификацию")

    def widthraw(self, amount):
        if self.is_autentificated == True:
            super().widthraw(amount)
        else:
            print("Необходимо пройти аутентификацию")

    def translate(self):
        eur = self.balance / 91
        usd = self.balance / 81
        print(f"Баланс в EUR: {eur}€")
        print(f"Баланс в USD: ${usd}")

def atm_menu(atm):
    while True:
        print("Меню банкомата")
        print("1. Проверить баланс")
        print("2. Внести деньги")
        print("3. Снять деньги")
        print("4. Пройти аутентификацию")
        print("5. Выход")
        print("6. Посмотреть баланс в EUR и USD")

        choice = input("Выберите действие:")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            summa = int(input("Введите сумму для пополнения: "))
            atm.widthraw(summa)
        elif choice == "3":
            summa == int(input("Введите сумму для снятия: "))
            atm.widthraw(summa)
        elif choice == "4":
            enter_pin = int(input("Введите Pin-code для входа: "))
            atm.autentificat(enter_pin)
        elif choice == "5":
            print("До свидания")
            break    
        elif choice == "6":
            atm.translate()
        else:
            print("Неправильный ввод")

pin = int(input("Установите Pin-code: "))
secure_atm = SecureATM(10000, pin)

enter_pin = int(input("Введите Pin-code для входа: "))
secure_atm.autentificat(enter_pin)

atm_menu(secure_atm)