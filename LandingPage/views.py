from django.shortcuts import render

# Create your views here.

def landing_page(request):
    return render(request, 'LandingPage/index.html')


def privacy_policy(request):
    return render(request, 'LandingPage/privacy_policy.html')


def terms_of_use(request):
    return render(request, 'LandingPage/terms_of_use.html')
