from djongo import models
from django import forms


class CostToCompany(models.Model):
    processing= models.CharField(max_length=50)
    gst= models.CharField(max_length=50)
    
    def __str__(self):
        return ''
    class Meta:
        abstract = True

class CosttoCompanyForm(forms.ModelForm):
    class Meta:
        model = CostToCompany
        fields = (
            '__all__'
        ) 


class Costing(models.Model):
    flags=models.BooleanField()
    calls=models.CharField( max_length=50)
    data=models.CharField( max_length=50)
    
    def __str__(self):
        return ''
    class Meta:
        abstract = True

class CostingForm(forms.ModelForm):
    class Meta:
        model = Costing
        fields = (
            '__all__'
        )  

class ClassCosting(models.Model):
    local= models.EmbeddedModelField(model_container = Costing, model_form_class=CostingForm)
    roaming= models.EmbeddedModelField(model_container = Costing, model_form_class=CostingForm)
    international= models.EmbeddedModelField(model_container = Costing, model_form_class=CostingForm)
    
    def __str__(self):
        return ''
    class Meta:
        abstract = True

class ClassCostingForm(forms.ModelForm):
    class Meta:
        model = ClassCosting
        fields = (
            '__all__'
        )    


class Others(models.Model):
    full_talktime= models.BooleanField()
    same_service_costing= models.EmbeddedModelField(model_container = ClassCosting, model_form_class=ClassCostingForm)
    different_service_costing= models.EmbeddedModelField(model_container = ClassCosting, model_form_class=ClassCostingForm)
    
    def __str__(self):
        return ''
    class Meta:
        abstract = True

class othersForm(forms.ModelForm):
    class Meta:
        model = Others
        fields = (
            '__all__'
        )


class Validity(models.Model):
    prepaid_validity= models.CharField(max_length=50)
    postpaid_duration= models.CharField(max_length=50)

    class Meta:
        abstract = True

class validityForm(forms.ModelForm):
    class Meta:
        model = Validity
        fields = (
            '__all__'
        )

class Plans(models.Model):
    _id = models.ObjectIdField()
    plans_name = models.CharField(max_length=250)
    plans_price = models.IntegerField()
    plan_type = models.CharField(max_length=50)
    talktime = models.CharField(max_length=50)
    data=models.CharField(max_length=50) 
    sms=models.CharField(max_length=50)
    validity = models.EmbeddedModelField(model_container = Validity, model_form_class= validityForm)
    costtocompany  = models.EmbeddedModelField(model_container = CostToCompany, model_form_class= CosttoCompanyForm)
    otherInfo = models.EmbeddedModelField(model_container = Others, model_form_class= othersForm)
    
    def __str__(self):
        return self.plans_name
