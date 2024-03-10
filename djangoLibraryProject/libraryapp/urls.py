from django.urls import path
from . import views as library_view
from consumer import views as consumer_view
urlpatterns = [    
    path('', library_view.LibraryView.as_view(), name="home"),
    path('libraryview/', library_view.LimitedBookListView.as_view(), name='limited-book-list'),
    path('library/', library_view.LibraryView.as_view(), name="library"),
    path('library/populate', library_view.LibraryPopulateView.as_view(), name="library-populate"),
    path('users/', library_view.UsersView.as_view(), name="users"),
    path('checkout/', library_view.Checkout.as_view(), name="checkout"),
    path('jobs/',consumer_view.JobsView.as_view(),name="jobs"),
    path('generate/',consumer_view.GenerateView.as_view(),name="generate"),  
]

login_urls = [
    path('login/', library_view.UserLogin.as_view(), name='login'),
    path('signup/', library_view.UserSignup.as_view(), name='signup'),
    path('logout/', library_view.UserLogout.as_view(), name='logout'),
] 
urlpatterns += login_urls