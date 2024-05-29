from django.urls import path
# from .views import Index
from website import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('ShowStaff/', views.ShowStaff, name="showStaff"),
    path('ShowStaffData/<int:id>/', views.ViewStaffData, name="viewStaffData"),    
]
