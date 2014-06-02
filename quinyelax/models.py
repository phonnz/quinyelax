# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class City(models.Model):
	idCity = models.AutoField(primary_key = True)
	name = models.CharField('Ciudad', max_length = 100)

	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name = 'Ciudad'
		verbose_name_plural = 'Ciudades'
		ordering = ('name', )

class Country(models.Model):
    idCountry = models.AutoField(primary_key=True)
    name = models.CharField('País', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

class Team(models.Model):
	idTeam = models.AutoField(primary_key = True)
	name = models.CharField('Nombre', max_length = 300)
	group_opts = (('A', 'Grupo A'),('B', 'Grupo B'), ('C', 'Grupo C'),('D', 'Grupo D'),('E', 'Grupo E'),('F', 'Grupo F'),('G', 'Grupo G'),('H', 'Grupo H'))
	group = models.CharField('Grupo', max_length=1,choices=group_opts,default='A')
	local_goals = models.PositiveIntegerField('Goles como local', default = 0, editable = False)
	visitant_goals = models.PositiveIntegerField('Goles como visitante', default = 0, editable = False)
	points = models.PositiveIntegerField('Puntos', default = 0, editable = False)
	firstPlace = models.BooleanField('Primero de grupo', default = False, editable = False)
	secondPlace = models.BooleanField('Segundo de grupo', default = False, editable = False)

	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name = 'Equipo'
		ordering = ('name', 'group')

class Match(models.Model):
	idMatch = models.AutoField(primary_key = True)
	localTeam = models.ForeignKey('Team', verbose_name = 'Local', related_name = 'local_id')
	visitantTeam = models.ForeignKey('Team', verbose_name = 'Visitante', related_name = 'visitant_id')
	hour = models.DateTimeField()
	city = models.ForeignKey(City, verbose_name = 'Ciudad')
	localGoals = models.PositiveIntegerField('Goles del local', default = 0)
 	visitantGoals = models.PositiveIntegerField('Goldes del visitante', default = 0 )
 	classify = models.BooleanField('Clasificación', default = False)

 	class Meta:
		verbose_name = 'Partido'
		ordering = ('hour', )


class Subscriber(models.Model):
	idSubscriber = models.AutoField(primary_key = True)
	email = models.EmailField('Correo')
	created = models.DateTimeField('Creado', editable = False, auto_now_add = True)
	updated = models.DateTimeField('Actualizado', editable = False, auto_now = True)


class UserData(models.Model):
	user = models.ForeignKey(User, verbose_name = 'Usuario')
	nick = models.CharField('Nick', max_length=100)
	bornDate = models.DateField('Fecha de Nacimiento')
	Country = models.ForeignKey('Country', verbose_name = 'País')
	created = models.DateTimeField('Creado', editable = False, auto_now_add = True)
	updated = models.DateTimeField('Actualizado', editable = False, auto_now = True)

 	class Meta:
		verbose_name = 'Suscriptor'
		verbose_name_plural = 'Suscriptores'
		ordering = ('created', )
