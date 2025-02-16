from django.urls import path
from .views import index, delete_data

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>', delete_data, name='delete_data'),

]
