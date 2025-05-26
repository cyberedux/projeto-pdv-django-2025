from django.shortcuts import render

from app.models import Produto

# Create your views here.
def produtos_view(request):
    # equivalente ao "SELECT * FROM Produto"
    produtos = Produto.objects.all()
    
    return render(request, 'produtos.html', {'produtos': produtos})

