from organize_my_account.common.choicesenum import ChoicesEnum


class TypeBankAccount(ChoicesEnum):
    CURRENT_ACCOUNT = 'CURRENT_ACCOUNT', 'Conta corrente'
    SAVINGS_ACCOUNT = 'SAVINGS_ACCOUNT', 'Conta poupança'