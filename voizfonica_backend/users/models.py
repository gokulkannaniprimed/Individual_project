from djongo import models
from django import forms
from django.contrib.auth.models import User
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads', filename)

class Proofs(models.Model):
    _id = models.ObjectIdField()
    proof = models.FileField(upload_to="uploads/", default='', blank=True, null=True)
    
    def __str__(self):
        return os.path.basename(self.proof.name)


class UserProfile(models.Model):
    
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address =models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    alternate_phone = models.CharField(max_length=254)
    kyc_verified = models.BooleanField()
    # accounts_linked = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    # transactions_linked = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    # tickets_linked = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    # cards_linked = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    proofs_attached = models.ArrayReferenceField(to=Proofs,
        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.id)
