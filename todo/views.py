from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from todo.models import TodoItem


# Create your views here.

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def index(request):
    if request.method == 'POST':
        TodoItem.objects.create(title=request.data['title'])
        return JsonResponse({"message": "Added successfully!"})
    items = TodoItem.objects.all().order_by('-updated_at')
    results = []
    for item in items:
        results.append({"id":item.id,"title": item.title, "completed": item.completed})
    return JsonResponse(results, safe=False)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_data(request, id):
    TodoItem.objects.filter(id=id).delete()
    return JsonResponse({"message": "Deleted successfully!"})

