from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('ciudadano/<int:pk>/', views.ciudadano_summary, name='ciudadano_summary'),
    path('ciudadano/<int:pk>/edit/', views.update_ciudadano, name='update_ciudadano'),
    path('list_users/', views.list_users, name='list_users'),
    path('consulta-antecedentes-ciudadano/', views.consulta_antecedentes_ciudadano, name='consulta_antecedentes_ciudadano'),
    path('consulta-mis-antecedentes/', views.consulta_mis_antecedentes, name='consulta_mis_antecedentes'),
]