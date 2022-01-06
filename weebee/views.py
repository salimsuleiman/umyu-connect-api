from django.urls.conf import path
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.shortcuts import render





@api_view(['GET'])
def docApi(request):
    print()
    return render(request,'api/index.html', {})