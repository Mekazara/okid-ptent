from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from okid_patent.forms import PrikazForm
from okid_patent.models import Prikaz
from .filters import PrikazFilter
from .forms import LoginForm


def prikazList(request):
    prikazy = Prikaz.objects.all()
    filter = PrikazFilter(request.GET, queryset=prikazy)
    prikazy = filter.qs
    amount = prikazy.count()
    context = {'prikazy': prikazy, 'amount': amount, 'filter': filter}
    return render(request, 'okid_patent/prikazy.html', context)

def auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('prikazy')

    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, 'okid_patent/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')


def createPrikaz(request):
    # user = request.user
    form = PrikazForm()
    if request.method == 'POST':
        form = PrikazForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prikazy')
        else:
            form = PrikazForm()
    context = {'form': form}
    return render(request, 'okid_patent/prikazcreate.html', context)

def editPrikaz(request, prikaz_id):
    prikaz = Prikaz.objects.get(id=prikaz_id)
    form = PrikazForm(instance=prikaz)
    if request.method == 'POST':
        form = PrikazForm(request.POST, request.FILES, instance=prikaz)
        if form.is_valid():
            form.save()
            return redirect('prikazy')
        else:
            form = PrikazForm(instance=prikaz)
    context = {'form': form}

    return render(request, 'okid_patent/editprikaz.html', context)

