from django.shortcuts import render,redirect
from.service import create

def home_page(request):
    return render(request ,'accueil.html')

def contact_page(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        objet = request.POST.get('objet')
        email = request.POST.get('email')
        message = request.POST.get('message')
        create(nom,objet,email,message, False)
        return redirect('app_home')

    return render(request, 'contact.html')

def service_page(request):
    return render(request, 'service.html')

def about_page(request):
    return render(request, 'about.html')

def admin_page(request):
    return render(request, 'admin.html')

# Create your views here.
