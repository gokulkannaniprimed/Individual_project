from django.contrib import admin
from .models import Problems,Ticket,Chat,Messages
#,Chat,Messages
# Register your models here.

admin.site.register(Chat)
admin.site.register(Problems)
admin.site.register(Ticket)
admin.site.register(Messages)
