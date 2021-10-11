from django.db import models

from .enums import TypeTransaction


class Transaction(models.Model):
    type_transaction = models.CharField(
        max_length=TypeTransaction.get_database_max_length(),
        default=TypeTransaction.CURRENT_ACCOUNT.value,
        choices=TypeTransaction.choices()
    )
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date_posted = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

