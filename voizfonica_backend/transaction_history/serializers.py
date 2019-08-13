from rest_framework import serializers
from .models import Transactions
from wallet.serializers import WalletSerializer
from card.serializers import CardSerializer
# from accounts.serializers import AccountSerializer


class TransactionsSerializer(serializers.ModelSerializer):
    wallet_linked = WalletSerializer()
    card_linked = CardSerializer()
    # for_account = AccountSerializer()
    
    class Meta:
        model = Transactions
        fields="__all__"
        # fields = ['transaction_amount','transaction_date_time','transaction_state',
        # # 'for_account',
        # 'wallet_linked','card_linked']

