from django.urls import path
from api import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
routers=DefaultRouter()
routers.register('v2/task',views.TaskviewSet,basename="task")
urlpatterns=[
    path("token",ObtainAuthToken.as_view()),
    path('register',views.SignupView.as_view()),
]+routers.urls