from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import DetailTodo, ListTodo

"""
router = SimpleRouter()
router.register('', TodoViewSet, base_name='todos')

urlpatterns = router.urls
"""

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
]
