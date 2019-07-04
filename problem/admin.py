from django.contrib import admin
from .models import Problem, Solve

# Register your models here.

admin.site.register(Problem)
admin.site.register(Solve)

import sys;

reload(sys);
sys.setdefaultencoding("utf8")
