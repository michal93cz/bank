class Kir:
    banks = []

    def make_transfer(self, destination_bank_id, money, account_id):
        try:
            bank = self.get_bank_by_id(destination_bank_id)
            return bank.outgoing_transfer(account_id, money)
        except ValueError:
            return False

    def add_bank(self, bank):
        self.banks.append(bank)
        bank.set_kir(self)

    def get_bank_by_id(self, id):
        for bank in self.banks:
            if bank.bank_id == id:
                return bank
        print("Bank with id is not exists")
        raise ValueError("Bank id is not exists")




