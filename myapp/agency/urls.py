from django.urls import path
from . import views


# defining a list of url patterns
urlpatterns = [
    path('', views.index, name= 'index'),
    path('home/',views.home_view, name = 'home' ),
    path('home/contact/', views.contact_view, name= 'contact' ),
    path('home/contact/success', views.contact_success_view, name= 'contact_success')

]



