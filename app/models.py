from django.db import models
from django.contrib.auth.models import User
# Django user model
'''
 - username
 - password
'''

class StudentDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname=models.CharField(max_length=30)
    mname=models.CharField(max_length=30)
    rollno=models.IntegerField()
    dob=models.DateTimeField()

    def __str__(self):
        return self.user.username


class TeacherDetails(models.Model):
    teacher = models.OneToOneField(User,on_delete=models.CASCADE)
    subject = models.TextField(max_length=100)
    is_principal = models.BooleanField(max_length=100)

    def __str__(self):
        return self.teacher.username

class Term1(models.Model):
    user = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
    rollno=models.IntegerField()
    phy=models.IntegerField(null=True)  
    chem=models.IntegerField(null=True)
    math=models.IntegerField(null=True)
    comp=models.IntegerField(null=True)
    eng=models.IntegerField(null=True)

    def __str__(self):
        return "{} term1 marks".format(self.user.user.username)

class Term2(models.Model):
    user = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
    rollno=models.IntegerField()
    phy=models.IntegerField(null=True)  
    chem=models.IntegerField(null=True)
    math=models.IntegerField(null=True)
    comp=models.IntegerField(null=True)
    eng=models.IntegerField(null=True)

    def __str__(self):
        return "{} term2 marks".format(self.user.user.username)

class Finals(models.Model):
    user = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
    rollno=models.IntegerField()
    phy=models.IntegerField(null=True)  
    chem=models.IntegerField(null=True)
    math=models.IntegerField(null=True)
    comp=models.IntegerField(null=True)
    eng=models.IntegerField(null=True)

    def __str__(self):
        return "{} final marks".format(self.user.user.username)

    

