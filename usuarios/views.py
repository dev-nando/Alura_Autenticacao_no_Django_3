from django.shortcuts import render, redirect

def cadastro(request):
    if request.method == 'POST':
        print('Usuário criado com sucesso')
        return redirect('login')
    return render(request,'usuarios/cadastro.html')

def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    pass