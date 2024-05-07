from django.shortcuts import render,redirect
from .models import *

def donorhome(request):
    foods=Food.objects.filter(donor=request.user)
    return render(request,"donorhome.html",{"foods":foods})

def addfood(request):
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        expiry_date=request.POST.get("expiry_date")
        pickup_address=request.POST.get("pickup_address")
        image=request.FILES.get("image")
        donor=request.user
        food =Food(name=name,description=description,expiry_date=expiry_date,pickup_address=pickup_address,image=image,donor=donor)
        food.save()
        return redirect("/donorhome")
    else:
        return render(request,"addfood.html")
    

def deletefood(request,pk):
    food=Food.objects.get(id=pk,donor=request.user)
    food.delete()
    return redirect("/donorhome")

def editfood(request,pk):
    food=Food.objects.get(id=pk,donor=request.user)
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        expiry_date=request.POST.get("expiry_date")
        pickup_address=request.POST.get("pickup_address")
        image=request.FILES.get("image")
        donor=request.user
        food.name=name
        food.description=description
        food.expiry_date=expiry_date
        food.pickup_address=pickup_address
        food.image=image
        food.donor=donor
        food.save()
        return redirect("/donorhome")
    else:
        return render(request,"editfood.html",{"food":food})
    

def requests(request):
    donor_foods = Food.objects.filter(donor=request.user)
    pending_requests = Request.objects.filter(food__in=donor_foods, status='pending')
    food_details = [{'food': req.food, 'user_email': req.user.email,"req_id":req.id} for req in pending_requests]
    print(food_details)
    return render(request, 'requests.html', {'food_details': food_details})


def acceptrequest(request,pk):
    req =Request.objects.get(id=pk)
    req.status = 'accepted'
    req.save()
    return redirect('/requests')



def rejectrequest(request,pk):
    req =Request.objects.get(id=pk)
    req.status = 'rejected'
    req.save()
    return redirect('/requests')








        