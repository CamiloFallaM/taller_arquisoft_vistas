from django.urls import path
from . import views

urlpatterns =  [
        path('list/', views.get_measurements, name='measurementList'),
        path('get/<int:pk>/', views.get_measurement, name='measurement'),
        path('delete/<int:pk>/', views.delete_measurement, name='measurement_delete'),
        path('update/<int:pk>/<int:new_value>/', views.update_measurement, name='measurement_update')

]