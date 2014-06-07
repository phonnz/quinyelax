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
 	classify = models.BooleanField('Clasificación', default = True)

 	def __unicode__(self):
		return self.localTeam.name + ' vs ' + self.visitantTeam.name

 	class Meta:
		verbose_name = 'Partido'
		ordering = ('hour', )


class Subscriber(models.Model):
	idSubscriber = models.AutoField(primary_key = True)
	email = models.EmailField('Correo')
	created = models.DateTimeField('Creado', editable = False, auto_now_add = True)
	updated = models.DateTimeField('Actualizado', editable = False, auto_now = True)

	def __unicode__(self):
		return self.email

class UserData(models.Model):
	User = models.ForeignKey(User, verbose_name = 'Usuario')
	nick = models.CharField('Nick', max_length=100)
	bornDate = models.DateField('Fecha de Nacimiento', null =  True, blank = True)
	Country = models.ForeignKey('Country', verbose_name = 'País', null =  True, blank = True)
	firstA = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_firstA')
	secondA = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_secondA')
	firstB = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_firstB')
	secondB = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_secondB')
	firstC = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_firstC')
	secondC = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_secondC')
	firstD = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_firstD')
	secondD = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_secondD')
	firstE = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_firstE')
	secondE = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_secondE')
	firstF = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_firstF')
	secondF = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_secondF')
	firstG = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_firstG')
	secondG = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_secondG')
	firstH = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_firstH')
	secondH = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_secondH')
	A = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_A')
	B = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_B')
	C = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_C')
	D = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_D')
	W = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_E')
	Z = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_F')
	X = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_G')
	Y = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_H')
	champ = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_champ')
	third = models.ForeignKey('Team', verbose_name = 'Equipo', null = True, blank = True, related_name = 'id_third')

	firstAResult = models.BooleanField('AciertoA', default = False)
	secondAResult = models.BooleanField('AciertoA', default = False)
	firstBResult = models.BooleanField('AciertoA', default = False)
	secondBResult = models.BooleanField('AciertoA', default = False)
	firstCResult = models.BooleanField('AciertoA', default = False)
	secondCResult = models.BooleanField('AciertoA', default = False)
	firstDResult = models.BooleanField('AciertoA', default = False)
	secondDResult = models.BooleanField('AciertoA', default = False)
	firstEResult = models.BooleanField('AciertoA', default = False)
	secondEResult = models.BooleanField('AciertoA', default = False)
	firstFResult = models.BooleanField('AciertoA', default = False)
	secondFResult = models.BooleanField('AciertoA', default = False)
	firstGResult = models.BooleanField('AciertoA', default = False)
	secondGResult = models.BooleanField('AciertoA', default = False)
	firstHResult = models.BooleanField('AciertoA', default = False)
	secondHResult = models.BooleanField('AciertoA', default = False)
	AResult = models.BooleanField('AciertoA', default = False)
	BResult = models.BooleanField('AciertoA', default = False)
	CResult = models.BooleanField('AciertoA', default = False)
	DResult = models.BooleanField('AciertoA', default = False)
	WResult = models.BooleanField('AciertoA', default = False)
	ZResult = models.BooleanField('AciertoA', default = False)
	XResult = models.BooleanField('AciertoA', default = False)
	YResult = models.BooleanField('AciertoA', default = False)
	champResult = models.BooleanField('AciertoA', default = False)
	thirdResult = models.BooleanField('AciertoA', default = False)

	created = models.DateTimeField('Creado', editable = False, auto_now_add = True)
	updated = models.DateTimeField('Actualizado', editable = False, auto_now = True)

	def __unicode__(self):
		return self.user.name

 	class Meta:
		verbose_name = 'Octavo'
		ordering = ('created', )

class UserGroup(models.Model):
	idUserGroup = models.AutoField(primary_key = True)
	user = models.ForeignKey(User, verbose_name = 'Dueño')
	name = models.CharField('Ganador' , max_length = 100)
	users = models.ManyToManyField(User,verbose_name = 'Ususarios', related_name = 'users_allowed')
	created = models.DateTimeField('Creado', editable = False, auto_now_add = True)
	updated = models.DateTimeField('Actualizado', editable = False, auto_now = True)

	def __unicode__(self):
		return self.email

	class Meta:
		verbose_name = 'Partido del participante'
		verbose_name_plural = 'Partidos del participante'


class UserMatch(models.Model):
	idUserMatch = models.AutoField(primary_key = True)
	User = models.ForeignKey(User)
	Match = models.ForeignKey('Match', verbose_name = 'Partido')
	winner = models.CharField('Ganador' , max_length = 3)
	created = models.DateTimeField('Creado', editable = False, auto_now_add = True)
	updated = models.DateTimeField('Actualizado', editable = False, auto_now = True)

	def __unicode__(self):
		return self.email

	class Meta:
		verbose_name = 'Partido del participante'
		verbose_name_plural = 'Partidos del participante'