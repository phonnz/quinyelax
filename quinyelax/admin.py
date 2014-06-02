# -*- coding: utf-8 -*-
from django.contrib import admin
from datetime import datetime
from models import *


admin.site.register(City)
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Subscriber)