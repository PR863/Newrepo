from django.urls import path
from . import views

urlpatterns = [
    path('lv/', views.CustumerView.as_view(), name='custumer_url'),
    path('sv/', views.ShowView.as_view(), name='display_url'),
    path('up/<int:pk>/', views.UpdateView.as_view(), name='update_url'),
    path('del/<int:pk>/', views.DeleteView.as_view(), name='delete_url')
]