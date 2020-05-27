from django.urls import path
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('country/<int:cid>/', views.country, name='country'),
    path('details/<int:cid>/', views.details, name='details'),
]
