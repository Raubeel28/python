from django.urls import path
#from .views import index
from . import views

urlpatterns=[
    #THis path was the one i used for the django site
  #  path('',index,name="index"),
    path('',views.home_view,name="home"),
    path('contact/',views.contact_view,name="contact"),
    path('success/',views.contact_success_view,name="contact-success"),

]

