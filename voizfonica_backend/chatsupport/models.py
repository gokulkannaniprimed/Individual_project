from django.db import models
from django.contrib.auth.models import User

sender_type_choices=(
     ('user','USER'),
     ('bot','BOT'),
)

message_type_choices=(
     ('information','INFORMATION'),
     ('option','OPTION'),
     ('null','NULL')
)

prob_choices = (
    ('info','INFO'),
    ('option','OPTION'),
)

tick_choices = (
    ('Open','OPEN'),
    ('Closed','CLOSED'),
)

class Chat(models.Model):
     user_id=models.CharField(max_length=100)
     ip_address=models.CharField(max_length=100)
     start_time=models.CharField(max_length=100)

class Messages(models.Model):
     chat_id=models.CharField(max_length=100)
     user_id=models.CharField(max_length=100)
     sender_type=models.CharField(max_length=50,choices=sender_type_choices,default='bot')
     message_content=models.TextField()
     message_type=models.CharField(max_length=50,choices=message_type_choices,default='null')
     time_stamp=models.CharField(max_length=50)

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
















#from transactions.model import Transactions

# Create your models here.






# class Transactions_for_support(Transactions)
#      refund_status=models.CharField(max_length=50)
#      raise_ticket=models.BooleanField()