from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login, authenticate, logout
from .models import Library
from .forms import RegisterUserForm, LoginForm
from django.views.generic import TemplateView,ListView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.serializers import serialize
from . import models
# Create your views here.

class UserSignup(TemplateView):
    template_name = 'registeruser.html'

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponse('<b>Registeration successfull!</b>')              
        
        return HttpResponse('<b style="color: red"> Registeration Failed!!  <br>Login id and Password must  satisfying all constraints. </br> </b> ')
    
    def get(self, request):
        form = RegisterUserForm()
        return render(request, 'registeruser.html', {'form': form})



class LibraryView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        template_name = 'library.html'
        all_books = Library.objects.all().values()
        context = {'books': all_books}
        return render(request, template_name, context=context)
    model = Library
    template_name = 'library.html'
    context_object_name = 'books'
    def get_queryset(self):
        limit = int(self.request.GET.get('limit',10))                
        if limit > 0:
         all_books = Library.objects.all()[:limit].values()
        else :
         all_books = Library.objects.all()
        context = {'books': all_books}
        return all_books


class UsersView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    def get(self, request):
        template_name = 'users.html'
        all_users = User.objects.all()
        context = {'users': all_users}
        return render(request, template_name, context=context)
    # UserPassesTestMixin :: define a test function that determines whether a user is allowed 
    # to view a particular page or perform an action .
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()
    

class LibraryPopulateView(LoginRequiredMixin, View):
    
    def get(self, request):
        Library.populate_library_data()
        return redirect('library')


class UserLogin(TemplateView):

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('library')
    
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


class UserLogout(LoginRequiredMixin, TemplateView):

    def get(self, request):
        logout(request)
        return redirect('login')

class Checkout(LoginRequiredMixin,View):

    def post(self, request):
        try:
            
            book_id = request.POST.get('pk')
            book = models.Library.objects.get(pk=book_id)
        except models.Library.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        if not book.is_in_stock:
            return Response({"error": "Book already checked out"}, status=status.HTTP_409_CONFLICT)

        book.is_in_stock = False
        book.save()  # Saves and updates dateCheckedOut
        newtr = f"<tr id='book-row-"+str(book.id)+"'><td>"+str(book.id)+"</td><td>"+book.title+"</td><td>"+book.author+"</td><td>"+str(book.date_checked_out)+"</td><td>"+str(book.is_in_stock)+"</td><td></td></tr>"
        return HttpResponse(newtr)


class QLimitedBookListView(ListView):   
    template_name = 'library.html'
    def get_queryset(self):
        limit = int(self.request.GET.get('limit', 10))
        return models.Library.objects.all()[:limit]

#http://127.0.0.1:8000/libraryview/?limit=20
class LimitedBookListView(LoginRequiredMixin, ListView):
    model = Library
    template_name = 'library.html'
    context_object_name = 'books'
    def get_queryset(self):
        limit = int(self.request.GET.get('limit',10))                
        if limit > 0:
         all_books = Library.objects.all()[:limit].values()
        else :
         all_books = Library.objects.all()
        context = {'books': all_books}
        return all_books
        