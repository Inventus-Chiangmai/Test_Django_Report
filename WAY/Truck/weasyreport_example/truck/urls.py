from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('generate/pdf/', views.generate_pdf, name='generate_pdf'),
    path('generate/truck_control/', views.truck_control_pdf, name='truck_control_pdf'),
    path('generate/truck_controls/', views.truck_controls_pdf, name='truck_controls_pdf'),
    path('generate/new/', views.new_pdf, name='new_pdf'),
    path('generate/delivery_note/', views.delivery_note_pdf, name='delivery_note_pdf'),
]