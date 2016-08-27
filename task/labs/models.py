from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser


class UserProfile(models.Model):  
    user = models.OneToOneField(User)
    address =  models.CharField(max_length=200)

    def __str__(self):
		return self.address

# class Patient(models.Model):
# 	name = models.CharField(max_length=200)
# 	national_id = models.CharField(max_length=200)
# 	address = models.CharField(max_length=200)

# 	def __str__(self):
# 		return self.name


class Bloodtest(models.Model):
	wbc = models.CharField(max_length=200)
	rbc = models.CharField(max_length=200)
	platelets = models.CharField(max_length=200)
	patient_id = models.ForeignKey(User,on_delete=models.CASCADE)
	

	def __str__(self):
		return 'WBC : %s ||  RBC: %s || Platelets: %s' % (self.wbc, self.rbc , self.platelets) 



class Livertest(models.Model):
	sgot = models.CharField(max_length=200)
	sgpt = models.CharField(max_length=200)
	albumin = models.CharField(max_length=200)
	patient_id = models.ForeignKey(User,on_delete=models.CASCADE)
	

	def __str__(self):
		return 'SGOT : %s ||  SGPT: %s || Albumin: %s' % (self.sgot, self.sgpt, self.albumin) 		