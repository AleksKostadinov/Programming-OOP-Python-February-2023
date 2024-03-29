class Account:
    def __init__(self, id_account: int, balance: int, pin: int):
        self.__id = id_account
        self.balance = balance
        self.__pin = pin

        # self.id = id
        # self.balance = balance
        # self.pin = pin

    # @property
    # def id(self):
    #     return self.__id
    #
    # @id.setter
    # def id(self, value):
    #     self.__id = value
    #
    # @property
    # def pin(self):
    #     return self.__pin
    #
    # @pin.setter
    # def pin(self, value):
    #     self.__pin = value

    def get_id(self, pin):
        if pin != self.__pin:
            return "Wrong pin"
        return self.__id

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
