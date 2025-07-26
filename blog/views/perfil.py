from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from ..models import Perfil, Post, Comentario
from ..forms import EditarPerfilFormulario, AvatarFormulario, BiografiaFormulario


@login_required
def perfil(request):
    user = request.user
    perfil = Perfil.objects.get(usuario=user)
    posts = Post.objects.filter(autor=user)
    comentarios = Comentario.objects.filter(autor=user)
    formularioBiografia = BiografiaFormulario(instance=perfil)

    return render(request, 'blog/perfil.html', {
        'perfil': perfil,
        'posts': posts,
        'comentarios': comentarios,
        'formularioBiografia': formularioBiografia
    })


@login_required
def agregarBiografia(request):
    perfil = Perfil.objects.get(usuario=request.user)

    if request.method == 'POST':
        form = BiografiaFormulario(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
    return redirect('perfil')


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = EditarPerfilFormulario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditarPerfilFormulario(instance=usuario)
    return render(request, 'blog/usuario/editar_perfil.html', {"form": form})


@login_required
def uploadAvatar(request):
    perfil = Perfil.objects.filter(usuario=request.user.id).first()
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = AvatarFormulario(instance=perfil)

    return render(request, 'blog/usuario/upload_avatar.html', {'form': form})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'blog/post/post_form.html'
    success_url = '/perfil/'

    def form_valid(self, form):
        form.instance.autor = self.request.user  # asignar autor actual antes de guardar
        return super().form_valid(form)
    

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post/post_list.html'  # crearás esta plantilla
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user).order_by('-fechaDeCreacion')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'blog/post/post_form.html'
    success_url = '/perfil/'
    
    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)  # sólo puede editar sus propios posts


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post/post_confirm_delete.html'
    success_url = '/perfil/'

    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)