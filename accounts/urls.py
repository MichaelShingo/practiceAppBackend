from .views import RegisterAPI, LoginAPI, UserDetailAPIView
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from knox.views import LoginView as KnoxOriginalLoginView

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    # path('login/', KnoxOriginalLoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('getUser/', UserDetailAPIView.as_view()),
]
