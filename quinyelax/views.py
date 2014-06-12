# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from models import *
from forms import SubscriberForm

def home(request):
    errorMsg = ''
    successMsg = ''

    if request.method == 'POST':
        form = SubscriberForm(request.POST, request.FILES)
        if form.is_valid():
            actualEmail = request.POST['email']
            user = Subscriber.objects.filter(email=actualEmail)
            if len(user) == 0:
                subscriber = form.save()
                user = Subscriber.objects.get(email=actualEmail)
                successMsg = 'Gracias por registrarte, pronto estarás recibiendo noticias.'

            else:
                errorMsg = 'Gracias por registrarte, pronto estarás recibiendo noticias.'

                form = SubscriberForm()
    else    :

        form = SubscriberForm()
    
    groups = []
    a = Team.objects.filter(group = 'A')
    b = Team.objects.filter(group = 'B')
    c = Team.objects.filter(group = 'C')
    d = Team.objects.filter(group = 'D')
    e = Team.objects.filter(group = 'E')
    f = Team.objects.filter(group = 'F')
    g = Team.objects.filter(group = 'G')
    h = Team.objects.filter(group = 'H')

    groups.append(a)
    groups.append(b)
    groups.append(c)
    groups.append(d)
    groups.append(e)
    groups.append(f)
    groups.append(g)
    groups.append(h)

    return render(request, 'index.html',{ 'groups':groups, 'form':form, 'errorMessage':errorMsg, 'successMessage':successMsg})


@login_required
def quiniela(request):
    errorMsg = ''
    successMsg = ''
    localTeam = ''
    visitantTeam = ''

    ##TODO create this on user register
    # matches = Match.objects.all()
    # for m in matches:
    #     um = UserMatch()
    #     um.User = request.user
    #     um.Match = m
    #     um.save()



    userMatches = UserMatch.objects.filter(User = request.user)#.order_by(Match__hour)
    print len(userMatches)
    for um in userMatches:
        print um.winner
        if um.winner == '':
            print um.Match.localTeam.name + um.Match.visitantTeam.name
            localTeam = um.Match.localTeam.name
            visitantTeam = um.Match.visitantTeam.name
            break

    if localTeam == '' or visitantTeam == '':
        return HttpResponseRedirect('/octavos')

    return render(request, 'quiniela.html', {'errorMessage':errorMsg, 'successMessage':successMsg, 'localTeam':localTeam, 'visitantTeam':visitantTeam})

def send_Mail(email):
	
	send_mail('Registro exitoso', u'Se registró %s' % email ,'quinyelax@effio.la', ('agonzalez@nyxtechnology.com',), fail_silently=False)