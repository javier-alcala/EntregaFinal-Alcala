from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from ..models import Post, Comentario
from ..forms import ComentarioForm


def explorar(request):
    query = request.GET.get("q")
    filtro = request.GET.get("filtro")
    posts = Post.objects.all().order_by('-fechaDeCreacion')
    if query:
        if filtro == "autor":
            posts = posts.filter(autor__username__icontains=query).order_by('-fechaDeCreacion')
        else:
            posts = posts.filter(titulo__icontains=query).order_by('-fechaDeCreacion')
    comentario_form = ComentarioForm()

    return render(request, "blog/explorar.html", {
        "posts": posts,
        "comentario_form": comentario_form
    })


def agregar_comentario(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            return redirect('explorar')
    return redirect('explorar')


class ComentarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comentario
    template_name = 'blog/comentario_confirm_delete.html'
    success_url = '/explorar/'

    def test_func(self):
        comentario = self.get_object()
        return self.request.user == comentario.autor