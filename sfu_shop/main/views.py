from django.shortcuts import render
from main.forms import UserLoginForm
# Create your views here.

def index(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            user_login = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            
            # ВЫВОДИМ В ТЕРМИНАЛ - это то, что вам нужно!
            print("=" * 50)
            print("ДАННЫЕ ИЗ ФОРМЫ СФУ:")
            print(f"Логин: {user_login}")
            print(f"Пароль: {user_password}")
            print("=" * 50)
            form.save()
            
            
            return 0
        else:
            form = UserLoginForm()
    return render(request=request, 
                  template_name='main/index.html', 
                  context={'form': form})

