#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django_facebook.models import FacebookProfileModel
from django_facebook import signals

SCHOOL_CHOICES = (
	('ITESM Campus Monterrey','ITESM Campus Monterrey'),
	('UDEM','UDEM'),
	('UANL','UANL'),
	('UR','UR'),
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
	school = models.CharField(max_length=50, blank=True, null=True, choices=SCHOOL_CHOICES)
	carrer = models.CharField(max_length=50, blank=True, null=True)
	facebook = models.CharField(max_length=50, blank=True, null=True)
	twitter = models.CharField(max_length=20, blank=True, null=True)
	#aditional fields
	calification = models.IntegerField(default=1)
	points = models.IntegerField(default=0)
	total_surveys = models.IntegerField(default=0)

	def __unicode__(self):
		return u'%s' % (self.name)

	def get_url(self):
		return '/student/%s' % (self.pk)


class Profile(FacebookProfileModel):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return u'%s' % (self.user)


	#Create profile when new user
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	#Create new student info by user
	#def facebook_register(sender, profile, facebook_data, **kwargs):
	#	student = Student.objects.create(name=profile.facebook_name, facebook=profile.facebook_profile_url)

	#Signal to create user profile
	post_save.connect(create_user_profile, sender=User)
	#signals.facebook_user_registered.connect(facebook_register, sender=User)

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
	date = models.DateField(auto_now_add=True)
	comment = models.ForeignKey(Comment)
	opinions = models.ManyToManyField(Opinion)

	def __unicode__(self):
		return u'%s' % (self.user)

	def get_grade(self):
		grade = 0
		for opinion in self.opinions.all():
			if opinion.value:
				grade += 1
		return grade

	def get_opinion1(self):
		return self.opinions.all()[0].value

	def get_opinion2(self):
		return self.opinions.all()[1].value

	def get_opinion3(self):
		return self.opinions.all()[2].value

	def get_opinion4(self):
		return self.opinions.all()[3].value

	def get_opinion5(self):
		return self.opinions.all()[4].value