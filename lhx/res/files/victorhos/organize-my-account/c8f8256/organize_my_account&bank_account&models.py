from django.db import models

from .enums import TypeBankAccount


class Bank(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=3)


class BankAccount(models.Model):
    bank = models.ForeignKey(Bank)
    agency = models.CharField(max_length=4)
    account = models.CharField(max_length=11)
    digit = models.CharField(max_length=1)
    type_account = models.CharField(
        max_length=TypeBankAccount.get_database_max_length(),
        default=TypeBankAccount.CURRENT_ACCOUNT.value,
        choices=TypeBankAccount.choices()
    )
