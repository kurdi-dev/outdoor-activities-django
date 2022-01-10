from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Activity, Category
from .forms import ActivityForm

# Create your views here.


def home(request):
    activities = Activity.objects.all()
    categories = Category.objects.all()
    context = {'activities':activities, 'categories': categories}
    return render(request,'home.html',context)

def activity(request,activity_id):
    activity = Activity.objects.get(id=activity_id)
    context = {'activity':activity}
    return render(request,'activity.html',context)
    
def create_activity(request):
    form = ActivityForm()
    
    if request.method == 'POST':
        print(request.POST)
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = { 'form': form }
    return render(request,'activity_form.html', context)


def update_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    form = ActivityForm(instance=activity)

    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity )
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'activity_form.html',context)

def delete_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    if request.method == "POST":
        activity.delete()
        return redirect('home')
    context = {'obj':activity, 'type':'activity'}
    return render(request,'delete.html', context)
