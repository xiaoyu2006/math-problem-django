from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Problem
from .forms import ProbForm, SolveForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_prob(request):
    probs=Problem.objects.all().order_by('-date_added')
    context={'problems': probs}
    return render(request, 'problems.html', context=context)

def show_prob(request, id):
    prob=get_object_or_404(Problem, id=id)
    solves=prob.solve_set.all().order_by('-date_added')
    context={'prob': prob, 'solves': solves}
    return render(request, 'problem.html', context=context)

def new_prob(request):
    if request.method!='POST':
        form=ProbForm()
    else:
        form=ProbForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('prob:probs')
            )
    context={'form': form}
    return render(request, 'add_prob.html', context=context)

def new_solve(request, id):
    prob=get_object_or_404(Problem, id=id)
    if request.method!='POST':
        form=SolveForm()
    else:
        form=SolveForm(request.POST)
        if form.is_valid():
            new_solve=form.save(commit=False)
            new_solve.problem=prob
            new_solve.save()
            return HttpResponseRedirect(
                reverse('prob:prob',args=[id])
            )
    context={'prob': prob, 'form': form}
    return render(request, 'add_solve.html', context=context)
