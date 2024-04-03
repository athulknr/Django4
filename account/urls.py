from django.urls import path
from . import views 
from account.views import jobdetail,addjob,applyjob
urlpatterns = [
    path('', views.index, name='index'),  
    path('login', views.login_view, name='login_view'),
    path('signup', views.signup, name='signup'),
    path('admin', views.admin, name='admin'),
    path('employee', views.employee, name='employee'),
    path('employer', views.employer, name='employer'),
    path('job', views.job, name='job'),
    path('jobs/add/', addjob, name='addjob'),
    path('jobs/<int:job_id>', jobdetail, name='jobdetail'),
    path('jobs/<int:job_id>', jobdetail, name='jobdetail'),
    path('<int:job_id>/applyjob/', applyjob, name='applyjob'),

    
]

