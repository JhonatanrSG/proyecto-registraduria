from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import UserForm, CiudadanoForm
from .models import Ciudadano


def register_view(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        ciudadano_form = CiudadanoForm(request.POST, request.FILES)

        if user_form.is_valid() and ciudadano_form.is_valid():
            identificacion = ciudadano_form.cleaned_data['identificacion']

            # Verificar si la identificación ya existe
            if Ciudadano.objects.filter(identificacion=identificacion).exists():
                messages.error(request, "Este número de identificación ya está registrado. Por favor, ingrese otro.")
                return render(request, 'ciudadanos/register.html', {'user_form': user_form, 'ciudadano_form': ciudadano_form})

            # Guardar el usuario y crear el perfil de ciudadano
            user = user_form.save()
            ciudadano = ciudadano_form.save(commit=False)
            ciudadano.user = user
            ciudadano.save()

            # Login automático después del registro
            login(request, user)
            messages.success(request, '¡Registro exitoso! Has iniciado sesión.')
            return redirect('ciudadano_summary', pk=ciudadano.pk)
        else:
            messages.error(request, 'Error en el formulario, por favor verifica los datos.')
    else:
        user_form = UserForm()
        ciudadano_form = CiudadanoForm()

    return render(request, 'ciudadanos/register.html', {'user_form': user_form, 'ciudadano_form': ciudadano_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Verificar si el usuario tiene un perfil de ciudadano
            try:
                ciudadano = Ciudadano.objects.get(user=user)
                return redirect('ciudadano_summary', pk=ciudadano.pk)
            except Ciudadano.DoesNotExist:
                messages.error(request, "El usuario no tiene un perfil asociado.")
                return redirect('login')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'ciudadanos/login.html')


@login_required
def ciudadano_summary(request, pk):
    ciudadano = get_object_or_404(Ciudadano, pk=pk)

    # Verificar permisos
    puede_ver_antecedentes_civiles = request.user.has_perm('ciudadanos.ver_antecedentes_civiles')
    puede_ver_mis_antecedentes = request.user.has_perm('ciudadanos.ver_mis_antecedentes')

    context = {
        'ciudadano': ciudadano,
        'puede_ver_antecedentes_civiles': puede_ver_antecedentes_civiles,
        'puede_ver_mis_antecedentes': puede_ver_mis_antecedentes,
    }

    return render(request, 'ciudadanos/summary.html', context)


@login_required
def update_ciudadano(request, pk):
    ciudadano = get_object_or_404(Ciudadano, pk=pk)
    if request.method == 'POST':
        form = CiudadanoForm(request.POST, request.FILES, instance=ciudadano)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('ciudadano_summary', pk=ciudadano.pk)
    else:
        form = CiudadanoForm(instance=ciudadano)
    return render(request, 'ciudadanos/edit_user.html', {'form': form})


@login_required
def list_users(request):
    users = User.objects.all()
    user_list = ', '.join([user.username for user in users])
    return HttpResponse(f"Usuarios registrados: {user_list}")


@login_required
def consulta_antecedentes_ciudadano(request):
    if not request.user.has_perm('ciudadanos.ver_antecedentes_civiles'):
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    ciudadanos = Ciudadano.objects.all()
    return render(request, 'ciudadanos/consulta_antecedentes_ciudadano.html', {'ciudadanos': ciudadanos})


@login_required
def consulta_mis_antecedentes(request):
    if request.user.is_authenticated:
        try:
            ciudadano = Ciudadano.objects.get(user=request.user)
            return render(request, 'ciudadanos/consulta_mis_antecedentes.html', {'ciudadano': ciudadano})
        except Ciudadano.DoesNotExist:
            return HttpResponseForbidden("No tienes un perfil de ciudadano asociado.")
    return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

