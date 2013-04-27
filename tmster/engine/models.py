from django.db import models
from django.contrib.auth.models import User

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
	name = models.CharField(max_lenght=40)
	school = models.CharField(max_lenght=2, choices=SCHOOL_CHOICES)
	facebook = models.CharField(max_lenght=50, blank=True, null=True)
	twitter = models.CharField(max_lenght=20, blank=True, null=True)

	def __unicode__(self):
		return u'%s' % (self.name)


class Profile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return u'%s' % (self.user)

class Opinion(models.Model):
	variant = models.CharField(max_lenght=2, choices=VARIANT_CHOICES)
	value = models.BooleanField()

	def __unicode__(self):
		return u'%s' % (self.value)


class Comment(models.Model):
	text = models.CharField(max_lenght=300)

	def __unicode__(self):
		return u'%s' % (self.text)

class Survey(models.Model):
	user = models.ForeignKey(User)
	student = models.ForeignKey(Student)
	comment = models.ForeignKey(Comment)
	opinion = models.ManyToManyField(Opinion)

	def __unicode__(self):
		return u'%s' % (self.user)


