from .forms import CustomRegistrerForm
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = CustomRegistrerForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New User Accuont created")
            return redirect("register")
    else:
        register_form = CustomRegistrerForm()
        
    return render(request, 'register.html', {'register_form': register_form})
    