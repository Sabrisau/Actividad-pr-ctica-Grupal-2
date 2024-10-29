from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f'La cuenta de {username} se ha creado con exito!')
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'registration/registro.html', {'form':form})

        

