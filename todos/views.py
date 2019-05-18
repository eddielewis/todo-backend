from rest_framework import viewsets
from rest_framework import generics


from .models import Todo
from .permissions import IsOwner
from .serializers import TodoSerializer


class OwnObjectsMixin():
    """
    Only returns objects that belongs to the current user. Assumes the object
    has a 'user' foreignkey to a User.
    """

    def get_queryset(self):
        user = self.request.user
        return super(OwnObjectsMixin, self).get_queryset().filter(owner=user)


class ListTodo(OwnObjectsMixin, generics.ListAPIView):
    #permission_classes = (IsOwner,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(OwnObjectsMixin, generics.RetrieveAPIView):
    #permission_classes = (IsOwner,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
