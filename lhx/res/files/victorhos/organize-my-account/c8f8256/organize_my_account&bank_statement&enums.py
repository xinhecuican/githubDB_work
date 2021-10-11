from organize_my_account.common.choicesenum import ChoicesEnum


class TypeTransaction(ChoicesEnum):
    CREDIT = 'CREDIT', 'Crédito'
    DEBIT = 'DEBIT', 'Débito'