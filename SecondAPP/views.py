from django.shortcuts import render

# Create your views here.

def get_details(request):
    return render(request, 'SecondAPP/ProductDetails.html')

