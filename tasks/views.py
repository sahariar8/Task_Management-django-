from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def manager_dashboard(request):
    return render(request, 'dashboard/manager-dashboard.html')

def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def test(request):
    context = {
        'name1': 'John',
        'name2': 'Jane',
        'name3': 'Doe',
        'name4': 'Smith',
        'name5': 'Emily',
    }
    
    return render(request,'test.html', context)
