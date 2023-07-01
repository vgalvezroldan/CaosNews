from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import CreatePost
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Crear Vistas AQUI

# Página de Inicio
def home(request):
    posts_page = Paginator(Post.objects.filter(published=True), 3) # 3 POSTS X PÁGINA 
    page = request.GET.get('page')
    posts = posts_page.get_page(page)
    aux = 'x' * posts.paginator.num_pages
    return render(request, 'news/home.html', {'posts': posts, 'aux': aux})


def post(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'news/details.html', {'post': post})
    except:
        return render(request, 'news/404.html')

# Página de filtrado de autor


def autor(request, author_id):
    try:
        author = get_object_or_404(User, id=author_id)
        return render(request, 'news/author.html', {'author': author})
    except:
        return render(request, 'news/404.html')


# Filtrado de categorías
def categoria(request, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
        return render(request, 'news/category.html', {'category': category})
    except:
        return render(request, 'news/404.html')


# Filtrado por fecha
def fecha(request, month_id, year_id):
    posts = Post.objects.filter(
        published=True, created__month=month_id, created__year=year_id)
    print(Post)
    return render(request, 'news/dates.html', {'posts': posts, 'month': month_id, 'year': year_id})

# Registrar usuario


def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password1']:
            try:
                # Registrando Usuario
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/gestion/')
            except IntegrityError:
                return render(request, 'registration/signup.html', {
                    'form': UserCreationForm,
                    "error": "Usuario ya Existe"
                })

        return render(request, 'registration/signup.html', {
            'form': UserCreationForm,
            "error": "Contraseñas no Coinciden"
        })


@login_required
def gestion(request):
    posts = Post.objects.all()
    return render(request, 'news/gestionNews' , {'posts': posts})
   
# VISTA AL CREAR POST
def crear_post(request):
    if request.method == 'GET':
        return render(request, 'news/crear.html', {
            'form': CreatePost()
        })
    else:
        try:
            form = CreatePost(request.POST, request.FILES)
            if form.is_valid():
                create_form = form.save(commit=False)
                create_form.save()
                form.save_m2m()
                return redirect('gestion')
        except ValueError:
            return render(request, 'news/crear.html', {
                'form': CreatePost(),
                'error': 'Provee datos válidos'
            })

# VISTA PARA DESCONECTARSE DE LA SESIÓN
def signout(request):
    logout(request)
    return redirect('home')

# VISTA PARA LOGEARSE
def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST
                     ['password'])
        
        if user is None:
            return render(request, 'registration/signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña es incorrecto'
        })

        else:
            login(request, user)
            return redirect('/gestion/')

# VISTA PARA MODIFICAR UN POST  
@login_required     
def modificar_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CreatePost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/gestion/', post_id=post_id)
    else:
        form = CreatePost(instance=post)

    return render(request, 'news/modificar_post.html', {'form': form})

@login_required
def eliminar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'El post ha sido eliminado.')
        return redirect('/gestion/')  
    return render(request, 'news/eliminar_post.html', {'post': post})