from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    import platform
    print(platform.python_version())
    for key, value in request.META.items():
        print('{} : {} '.format(key,value))
    print('---111------')
    print(request.META.get('HTTP_ENV_CHECK_ACCESS_TOKEN'))
    print('-----222----')
    return HttpResponse("Hello, world. You're at the polls index.")