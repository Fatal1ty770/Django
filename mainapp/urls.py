from .views import main, products, contact
from django.urls import path

urlpatterns = [
    path('', main),
    path('contact/', contact),
    path('products/', products),

]
