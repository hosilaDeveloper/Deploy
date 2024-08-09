from django.urls import path
from .views import TodoDetailView, TodoView

urlpatterns = [
    path('', TodoView.as_view(), name='todo-list'),
    path('<int:pk>/detail/', TodoDetailView.as_view(), name='todo-detail'),
]
