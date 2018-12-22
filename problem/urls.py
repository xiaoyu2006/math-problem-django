from django.conf.urls import include, url

from . import views

urlpatterns = [
    # Homepage
    url(r'^$', views.index, name='index'),
    # Show all problems
    url(r'^problems$', views.all_prob, name='probs'),
    # Sow details of one problem
    url(r'^problem/(?P<id>\d+)$', views.show_prob, name='prob'),
    # Add one problem
    url(r'^new_prob$', views.new_prob, name='new_prob'),
    # Add one solve
    url(r'^new_solve/(?P<id>\d+)$', views.new_solve, name='new_solve')
]