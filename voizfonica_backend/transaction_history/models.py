from djongo import models
from wallet.models import Wallet
from card.models import Card
# from accounts.models import Account



class Transactions(models.Model):
    _id=models.ObjectIdField()
    transaction_amount=models.IntegerField()
    transaction_date_time=models.DateTimeField()
    transaction_state=models.CharField(max_length=50)
    # for_account = models.ForeignKey(accounts,on_delete=models.CASCADE)
    wallet_linked = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    card_linked = models.ForeignKey(Card, on_delete=models.CASCADE)


