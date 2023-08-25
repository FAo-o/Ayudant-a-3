from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('eliminarFact/<fact_text>',views.eliminarFact),
    path('edicionFact/<fact_text>',views.edicionFact),
    path('editarFact/<fact_text>/', views.editarFact, name='editar_fact'),
]
