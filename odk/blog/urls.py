from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='My blog'),
    path("blogpost/<int:id>",views.blogpost,name='blogpost'),
    path("signup",views.handlesignup,name='handlesignup')
]
