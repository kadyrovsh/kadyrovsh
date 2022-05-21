from django.shortcuts import render, redirect
from .models import *

def All_Fan(requests):
    if requests.method == "POST":
        Fan.objects.create(
            nom=requests.POST.get("n"),
            yonalish=Yonalish.objects.get(requests.POST.get("y")),
            # ustoz=Ustoz.objects.get(requests.POST.get("u"))
        )
        return redirect("/fanlar/")
    data = {
        "Fanlar":Fan.objects.all(),
        "yonalishlar":Yonalish.objects.all(),
        "ustozlar":Ustoz.objects.all()
    }
    return render(requests, "fanlar.html", data)

def fan_ochir(request, fan):
    Fan.objects.filter(id=fan).delete()
    return redirect("/fanlar/")

def All_Yonalish(requests):
    if requests.method == "POST":
        Yonalish.objects.create(
            name=requests.POST.get("n"),
            start_date=requests.POST.get("s_d"),
            is_active=requests.POST.get("i_a")
        )
        return redirect("/yonalishlar/")
    y = Yonalish.objects.all()
    return render(requests, "yonalishlar.html", {"Yonalish" : y})

def All_Ustoz(request):
    if request.method == "POST":
        Ustoz.objects.create(
            ism=request.POST.get("i"),
            familiya=request.POST.get("f"),
            malumot=request.POST.get("m")
        )
        return redirect("/ustozlar/")
    u = Ustoz.objects.all()
    return render(request, "ustozlar.html", {"Ustoz" : u})

def ustoz_ochir(request, u):
    Ustoz.objects.filter(id=u).delete()
    return redirect("/ustozlar/")

def yonalish_ochir(request, y_o):
    Yonalish.objects.filter(id=y_o).delete()
    return redirect("/yonalishlar/")

def yonalish_edit(request, pk):
    if request.method == "POST":
        Yonalish.objects.filter(id=pk).update(
            name=request.POST.get("n"),
            is_active=request.POST.get("i_a"),
        )
        return redirect("/yonalishlar/")
    data = {
        "y": Yonalish.objects.get(id=pk)
    }
    return render(request, "yonalish_edit.html", data )

def ustoz_edit(request, pk):
    if request.method == "POST":
        Ustoz.objects.filter(id=pk).update(
            ism = request.POST.get("i"),
            familiya = request.POST.get("f"),
            malumot = request.POST.get("m")
        )
        return redirect("/ustozlar/")
    data = {
        "u": Ustoz.objects.get(id=pk)
    }
    return render(request, "ustoz_edit.html", data)

