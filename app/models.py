from django.db import models
from django.contrib.auth.models import User
# Django user model
'''
 - username
 - password
'''

class FacultyDetails(models.Model):
    faculty = models.OneToOneField(User, on_delete=models.CASCADE)
    subject1=models.CharField(max_length=30)
    subject2=models.CharField(max_length=30)

    def __str__(self):
        return self.faculty.username


class HODDetails(models.Model):
    HOD = models.OneToOneField(User,on_delete=models.CASCADE)
    subject = models.TextField(max_length=100)

    def __str__(self):
        return self.HOD.username


class AdminDetails(models.Model):
    Admin = models.OneToOneField(User,on_delete=models.CASCADE)
    subject = models.TextField(max_length=100)

    def __str__(self):
        return self.Admin.username


# class Term1(models.Model):
#     user = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
#     rollno=models.IntegerField()
#     phy=models.IntegerField(null=True)  
#     chem=models.IntegerField(null=True)
#     math=models.IntegerField(null=True)
#     comp=models.IntegerField(null=True)
#     eng=models.IntegerField(null=True)

#     def __str__(self):
#         return "{} term1 marks".format(self.user.user.username)

# class Term2(models.Model):
#     user = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
#     rollno=models.IntegerField()
#     phy=models.IntegerField(null=True)  
#     chem=models.IntegerField(null=True)
#     math=models.IntegerField(null=True)
#     comp=models.IntegerField(null=True)
#     eng=models.IntegerField(null=True)

#     def __str__(self):
#         return "{} term2 marks".format(self.user.user.username)

# class Finals(models.Model):
#     user = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
#     rollno=models.IntegerField()
#     phy=models.IntegerField(null=True)  
#     chem=models.IntegerField(null=True)
#     math=models.IntegerField(null=True)
#     comp=models.IntegerField(null=True)
#     eng=models.IntegerField(null=True)

#     def __str__(self):
#         return "{} final marks".format(self.user.user.username)

    

