# -*- coding: utf-8 -*-
from django.contrib import admin
from datetime import datetime
from models import *
from django.db.models import Q

def calculatePoints(group, classify):
	if classify:
		teams = Team.objects.filter(group = group)
		
		for t in teams:
			t.firstPlace = False
			t.secondPlace = False

			matches = Match.objects.filter( Q(localTeam = t) | Q(visitantTeam = t) )
			
			t.points = 0
			t.local_goals = 0
			t.visitant_goals = 0
			for m in matches:

				##Goals counter
				if t == m.localTeam:
					t.local_goals += m.localGoals

				else:
					t.visitant_goals += m.visitantGoals

				##point obtaining
				if m.localGoals == 	m.visitantGoals:
					t.points += 1

				elif m.localGoals > m.visitantGoals:
					if t == m.localTeam:
						t.points += 3

				else:
					if t == m.visitantTeam :
						t.points += 3
			
			t.save()

		##Obtain rank on group
		teams = Team.objects.filter(group = group).order_by('points').reverse()[:2]

		if not teams[0].points == teams[1].points or (teams[0].points == teams[1].points and teams[0].visitant_goals > teams[1].visitant_goals):

			team = Team.objects.get(pk = teams[0].idTeam)
			team.firstPlace = True
			team.save()

			team = Team.objects.get(pk = teams[1].idTeam)
			team.secondPlace = True
			team.save()

		elif teams[0].visitant_goals < teams[1].visitant_goals:
			team = Team.objects.get(pk = teams[0].idTeam)
			team.secondPlace = True
			team.save()

			team = Team.objects.get(pk = teams[1].idTeam)
			team.firstPlace = True
			team.save()
		else:
			print 'error'



class MatchAdmin(admin.ModelAdmin):
	list_display = ('idMatch', 'marcador', 'hour', 'city', 'localGoals', 'visitantGoals', 'classify')
	# list_filter = ( 'approved', 'timestamp','user')
	#search_fields = ('latitude', 'longitude', 'user__username', 'audioDescription', 'audioName')
	list_editable = ('localGoals', 'visitantGoals','classify')

	def marcador(self, obj):
		return obj.localTeam.name + ' ' + str(obj.localGoals) + ' - ' + str(obj.visitantGoals) + ' ' + obj.visitantTeam.name

	def save_model(self, request, obj, form, change):
		obj.save()
		if obj.classify:
			calculatePoints(obj.localTeam.group, obj.classify)
		

class TeamAdmin(admin.ModelAdmin):
	list_display = ('idTeam', 'name', 'points', 'local_goals', 'visitant_goals', 'group', 'firstPlace','secondPlace')
	# list_filter = ( 'approved', 'timestamp','user')
	#search_fields = ('latitude', 'longitude', 'user__username', 'audioDescription', 'audioName')
	#list_editable = ('localGoals', 'visitantGoals','classify')

	

admin.site.register(City)
admin.site.register(Match,MatchAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Subscriber)