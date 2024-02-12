from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status,generics
from rest_framework.response import Response
from .serializers import MenuSerializer,BookingSerializer
from .models import MenuItem,Booking
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


# Create your views here.
 
def sayHello(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    #permission_classes = [permissions.IsAuthenticated] 