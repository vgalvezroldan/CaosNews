from django.urls import path
from .views import home, post, autor, categoria, fecha, signup, gestion, signout, signin, crear_post, modificar_post, eliminar_post


urlpatterns= [
    # PAGINA DE INICIO/HOME
    path('', home, name='home'),

    # PAGINA DE CONTENIDO POST
    path('post/<int:post_id>', post, name='post'),

    # PAGINA FILTRADO DE AUTOR
    path('autor/<int:author_id>', autor, name='autor'),

    # PAGINA DE FILTRADO CATEGORIA
    path('categoria/<int:category_id>', categoria, name='categoria'),

    # PAGINA DE FILTRADO POR FECHA
    path('fecha/<int:month_id>/<int:year_id>', fecha , name='fecha'),

    # PAGINA DE FORMULARIO LOGIN
    path('signup/', signup ,name='signup'),

    # PAGINA DE GESTION
    path('gestion/', gestion, name='gestion'),

    # RUTA AL CREAR UN POST
    path('gestion/crear', crear_post , name='crear_post'),

    path('logout/', signout , name='logout'),

    path('signin', signin, name='signin'),

    path('posts/<int:post_id>/modificar/', modificar_post, name='modificar_post'),

    path('posts/<int:post_id>/eliminar/', eliminar_post, name='eliminar_post'),

]

