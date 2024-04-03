from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm,AddJobForm,ApplicationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from account.models import Job,Application

# Create your views here.


def index(request):
    return render(request, 'index.html')
def signup(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form': form, 'msg':msg})       
    
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            elif user is not None and user.is_employer:
                login(request, user)
                return redirect('employer')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'        
    return render(request, 'login.html',{'form':form,'msg':msg})
def admin(request):
    return render(request,'admin.html')
def employee(request):
    return render(request,'employee.html')
def employer(request):
    return render(request,'employer.html')
def job(request):
    jobs = Job.objects.all()[0:3]
    return render(request, 'job.html',{'jobs': jobs})
def jobdetail(request, job_id) :
    job = Job.objects.get(pk=job_id)
    return render(request, 'jobdetail.html',{'job': job})
@login_required
def addjob(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('employer')
    else:  # Handle GET request by providing an empty form
        form = AddJobForm()

    return render(request, 'addjob.html', {'form': form})
@login_required
def applyjob(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            return redirect('employee')
    else:
        form = ApplicationForm()

    return render(request, 'applyjob.html', {'form': form, 'job': job})