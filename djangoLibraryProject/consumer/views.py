from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView,ListView
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.models import User
from django.core.serializers import serialize
from libraryapp.models import Jobs
from django_htmx.middleware  import HtmxDetails
from huey import crontab
from huey.contrib.djhuey import task, periodic_task, db_task, on_commit_task
from .tasks import generate_books_task
class JobsView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    def get(self, request):
        alljobs = Jobs.objects.all().values()       
        context = {'jobs': alljobs,'i': list(range(1,12))}
        
        if request.htmx:
            return render(request, "jobstable.html", context=context)
        else:   
            return render(request, "jobs.html", context=context)
    # UserPassesTestMixin :: define a test function that determines whether a user is allowed 
    # to view a particular page or perform an action .
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()


class GenerateView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    def get(self, request):
        jobinstance = Jobs.objects.create(
              user = self.request.user.username,
              status = "PENDING",
            )
        generate_books_task(jobinstance.jobid)
        #create task    
        return redirect( 'jobs')
    # UserPassesTestMixin :: define a test function that determines whether a user is allowed 
    # to view a particular page or perform an action .
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()