import json
from django.http import JsonResponse
from accounts.forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import get_messages
from django.contrib import messages
from django.shortcuts import render, redirect
from velas.models import Carrinho, ItemCarrinho, Produto

def register_view(request):
    storage = get_messages(request)
    for _ in storage:
        pass

    user_form = CustomUserCreationForm()

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            messages.success(request, f'Seja bem vindo {user}')
            return redirect('home')
            
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register.html', {'user_form':user_form})

def login_view(request):
    storage = get_messages(request)
    for _ in storage:
        pass

    login_form = CustomAuthenticationForm()

    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Login realizado com sucesso! Seja bem vindo {email}')

            carrinho, created = Carrinho.objects.get_or_create(usuario=user)

            local_cart = request.POST.get("local_cart")

            if local_cart:
                try:
                    local_cart = json.loads(local_cart)
                    for item in local_cart:
                        produto = Produto.objects.get(id=item["id"])
                        essence = item.get("essence", "")

                        item_existente = ItemCarrinho.objects.filter(carrinho=carrinho, produto=produto).first()

                        if item_existente:
                            item_existente.quantidade += item["quantity"]
                            item_existente.save()
                        else:
                            ItemCarrinho.objects.create(
                                carrinho=carrinho,
                                produto=produto,
                                quantidade=item["quantity"],
                                preco_unitario=produto.preco  # Ajuste conforme necessário
                            )
                except Exception as e:
                    print(f"Erro ao sincronizar carrinho: {e}")

            return JsonResponse({"status": "success"})  # Responde para o JavaScript limpar o localStorage
        else:
            messages.error(request, "Email ou senha inválidos.")

    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    storage = get_messages(request)
    for _ in storage:
        pass

    logout(request)
    messages.success(request, "Você saiu com sucesso.")
    return redirect('home')
