#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django_facebook.models import FacebookProfileModel

SCHOOL_CHOICES = (
	('1','ITESM Campus Monterrey'),
	('2','UDEM'),
	('3','UANL'),
	('4','UR'),
	)

VARIANT_CHOICES = (
	('1','Puntualidad'),
	('2','Desempeño'),
	('3','Accesibilidad'),
	('4','Personalidad'),
	('5','Recomendable'),
	)

class Student(models.Model):
	name = models.CharField(max_length=40)
	school = models.CharField(max_length=2, choices=SCHOOL_CHOICES)
	facebook = models.CharField(max_length=50, blank=True, null=True)
	twitter = models.CharField(max_length=20, blank=True, null=True)

	def __unicode__(self):
		return u'%s' % (self.name)


class Profile(FacebookProfileModel):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return u'%s' % (self.user)


	#Create profile when new user
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	#Create new student info by user
	def create_student_by_user(sender, instance, created, **kwargs):
		if created and instance.profile.facebook_name is not None:
			Student.objects.create(name=instance.profile.facebook_name, facebook=instance.profile.facebook_profile_url)

	#Signal to create user profile
	post_save.connect(create_user_profile, sender=User)
	#Signal to create new student 
	post_save.connect(create_student_by_user, sender=User)

class Opinion(models.Model):
	variant = models.CharField(max_length=2, choices=VARIANT_CHOICES)
	value = models.BooleanField(default=False)

	def __unicode__(self):
		return u'%s' % (self.value)


class Comment(models.Model):
	text = models.CharField(max_length=300)

	def __unicode__(self):
		return u'%s' % (self.text)

class Survey(models.Model):
	user = models.ForeignKey(User)#from
	student = models.ForeignKey(Student)#to
	comment = models.ForeignKey(Comment)
	opinions = models.ManyToManyField(Opinion)

	def __unicode__(self):
		return u'%s' % (self.user)


