from velas.models import Categoria

def categorias_dropdown(request):
    categorias = Categoria.objects.all()
    return{'categorias':categorias}