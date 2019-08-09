from django.db import models
from django.contrib.auth.models import User
#from transactions.model import Transactions

# Create your models here.
prob_choices = (
    ('info','INFO'),
    ('option','OPTION'),
)

tick_choices = (
    ('Open','OPEN'),
    ('Closed','CLOSED'),
)

# class Chat(models.Model):
#      status=models.BooleanField()

#      def __str__(self):
#           return str(self.id)

class Problems(models.Model):
     problems=models.CharField(max_length=100)
     solutions=models.CharField(max_length=100)
     type=models.CharField(max_length=10, choices=prob_choices, default='option')

     def __str__(self):
          return (self.problems)+' / '+(self.solutions)

class Ticket(models.Model):
     #user=models.ForeignKey(User,on_delete=models.CASCADE)
     ticket_type=models.CharField(max_length=100)
     ticket_issue_date=models.CharField(max_length=100)
     ticket_resolution_proposed_date=models.CharField(max_length=100)
     ticket_resolved_date=models.CharField(max_length=100)
     ticket_resolution_response=models.CharField(max_length=100)
     ticket_re_action_reason=models.CharField(max_length=100)
     ticket_status=models.CharField(max_length=50,choices=tick_choices, default='Open')
     chat=models.CharField(max_length=100)
     #transactions_linked=models.ForeignKey(Transactions,on_delete=models.CASCADE)
     #accounts_linked=models.ForeignKey(Accounts,on_delete=models.CASCADE)
     #chat_id=models.ForeignKey(Chat,on_delete=models.CASCADE)

     def __str__(self):
          return str(self.ticket_type)

# class Messages(models.Model):
#      chat_id=models.ForeignKey(Chat,on_delete=models.CASCADE)
#      user_id=models.ForeignKey(User,on_delete=models.CASCADE)
#      message=models.TextField()
#      sent_time=models.DateTimeField()
#      receive_time=models.DateTimeField()

#      def __str__(self):
#           return str(self.id)

#class Transactions_for_support(Transactions)
     #refund_status=models.CharField(max_length=50)
     #raise_ticket=models.BooleanField()