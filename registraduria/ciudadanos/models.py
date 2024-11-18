from django.apps import AppConfig
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission

class Ciudadano(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)  # Ahora es obligatorio
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=100)
    fecha_expedicion = models.DateField()
    lugar_expedicion = models.CharField(max_length=100)
    rh = models.CharField(max_length=3)
    grupo_sanguineo = models.CharField(max_length=3)
    estatura = models.FloatField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)  # Nuevo campo para el correo electrónico

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        permissions = [
            ('ver_mis_antecedentes', 'Puede ver sus propios antecedentes'),
            ('ver_antecedentes_civiles', 'Puede ver antecedentes civiles de otros'),
        ]

# models.py o apps.py

class CiudadanosConfig(AppConfig):
    name = 'ciudadanos'

    def ready(self):
        from django.db.models.signals import post_migrate
        from django.db import models

        @post_migrate.connect
        def create_permissions(sender, **kwargs):
            Permission.objects.get_or_create(codename='consultar_antecedentes_ciudadano', name='Puede consultar antecedentes de ciudadano')
            Permission.objects.get_or_create(codename='consultar_mis_antecedentes', name='Puede consultar sus propios antecedentes')

            # Crear grupo Registraduria_Usuarios
            registraduria_group, created = Group.objects.get_or_create(name='Registraduria_Usuarios')

            # Asignar permisos (ajusta los permisos según tus vistas)
            # Asegúrate de crear permisos específicos para las vistas que necesitas controlar.
            permission_antecedentes_civiles = Permission.objects.get(
                codename='ver_antecedentes_civiles')  # Ajusta el codename
            permission_consulta_mis_antecedentes = Permission.objects.get(
                codename='ver_mis_antecedentes')  # Ajusta el codename

            # Agregar permisos al grupo
            registraduria_group.permissions.add(permission_antecedentes_civiles, permission_consulta_mis_antecedentes)


