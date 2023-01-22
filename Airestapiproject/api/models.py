from django.db import models


# Create your models here.
class Company(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    about = models.TextField(max_length=200)
    type = models.CharField(max_length=100, choices=(('IT', 'IT'),
                                                      ('Non IT', 'Non IT'),
                                                      ('Mobile phone', 'Mobile phone')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name +"   "+ self.location 




class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    postion=models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('software Developer',"Soft"),
        ('Project Manager','pm')
    ))  
    company=models.ForeignKey(Company,on_delete=models.CASCADE)  
