from djongo import models
from django import forms

class Card(models.Model):
    no=models.IntegerField()
    expiry=models.IntegerField()
    cvv=models.IntegerField()
    

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = (
            'no', 'expiry','cvv'
        )

class Wallet(models.Model):
    type = models.CharField(max_length=200)
    id = models.IntegerField()

    class Meta:
        abstract=True

class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = (
            'type','id'
        )

class PaymentInfo(models.Model):
    card = models.EmbeddedModelField(
        model_container=Card,
        model_form_class=CardForm
    )
   
    wallet = models.EmbeddedModelField(
        model_container=Wallet,
        model_form_class=WalletForm
    )
    def __str__(self):
        return ''
    class Meta:
        abstract = True

class PaymentInfoForm(forms.ModelForm):
    class Meta:
        model = PaymentInfo
        fields = (
            '__all__'
        )



class Users(models.Model):
    username = models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    subscriber_id= models.IntegerField()
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    primary_phone_no= models.IntegerField()
    alternate_phone_no= models.IntegerField()
    address=models.CharField(max_length=100)
    circle=models.CharField(max_length=100)
    payment_info = models.EmbeddedModelField(model_container = PaymentInfo, model_form_class= PaymentInfoForm)
    proofs_attached = models.ImageField(default='ID.jpg',upload_to='proofs')
       

    
    def __str__(self):
        return self.users_username






# Create your models here.
