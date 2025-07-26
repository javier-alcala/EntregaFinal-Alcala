from .models import Perfil

def avatar_en_contexto(request):
    if request.user.is_authenticated:
        try:
            perfil = Perfil.objects.get(usuario=request.user)
            return {'perfil': perfil}
        except Perfil.DoesNotExist:
            return {}
    return {}