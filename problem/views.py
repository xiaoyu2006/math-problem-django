from os.path import abspath

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Problem
from .forms import ProbForm, SolveForm

# Some functions
def uploadimg(img_name):
    from qiniu import Auth, put_file, etag
    import qiniu.config
    access_key='hf_OTa2nV0Taho84tpokRzn6Gm58mrjwu5QOPHGw'
    secret_key='-uwYx2tXAsUpSssc5YRH026F8qlzt_h5qCpC3OFK'
    q=Auth(access_key, secret_key)
    bucket_name='idup'
    key='math-problem-proj/'+img_name.split('/')[-1]
    # 2592000s refers to 30d
    token=q.upload_token(bucket_name, key, 2592000)
    localfile=img_name
    ret,info=put_file(token, key, localfile)
    print(info)
    assert ret['key']==key
    assert ret['hash']==etag(localfile)

def getimg(img_name):
    # import requests
    from qiniu import Auth
    access_key='hf_OTa2nV0Taho84tpokRzn6Gm58mrjwu5QOPHGw'
    secret_key='-uwYx2tXAsUpSssc5YRH026F8qlzt_h5qCpC3OFK'
    q = Auth(access_key, secret_key)
    key='math-problem-proj/'+img_name.split('/')[-1]
    base_url = 'http://%s/%s' % ('assets.nemoworks.info', key)
    private_url = q.private_download_url(base_url, expires=2592000)
    # print(private_url)
    # r = requests.get(private_url)
    # assert r.status_code == 200
    return private_url


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
    if prob.img:
        context['img_url']=getimg(prob.img.name)
    return render(request, 'problem.html', context=context)

def new_prob(request):
    if request.method!='POST':
        form=ProbForm()
    else:
        form=ProbForm(request.POST, request.FILES)
        if form.is_valid():
            probobj=form.save(commit=False)
            form.save()
            uploadimg(abspath('media/%s'%(probobj.img.name)))
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
