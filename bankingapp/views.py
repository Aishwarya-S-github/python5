from django.shortcuts import render

# Create your views here.
# from . models import Name
def demo(request):
    # obj=Place.objects.all()
    # obj2=Name.objects.all()
    return render(request,'index.html')
