from django.urls import path
from django.contrib.auth.views import LogoutView
from blog.views.inicio import inicio, sobreMi
from blog.views.perfil import perfil, agregarBiografia, editarPerfil, uploadAvatar, PostCreateView, PostListView, PostUpdateView, PostDeleteView
from blog.views.usuario import login_request, register
from blog.views.explorar import explorar, agregar_comentario, ComentarioDeleteView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobreMi/', sobreMi, name='sobreMi'),

    path('perfil/', perfil, name='perfil'),
    path('perfil/biografia/', agregarBiografia, name='agregarBiografia'),
    path('perfil/editar/', editarPerfil, name='editarPerfil'),
    path('perfil/avatar/', uploadAvatar, name='upload_avatar'),
    
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/nuevo/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_delete'),

    path('login/', login_request, name="login"),
    path('registro/', register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='blog/usuario/logout.html'), name='logout'),

    path('explorar/', explorar, name='explorar'),
    path('comentario/<int:pk>/nuevo/', agregar_comentario, name='agregar_comentario'),
    path('comentario/<int:pk>/eliminar/', ComentarioDeleteView.as_view(), name='comentario_delete'),
]