from django.urls import path

from item.views import CreateEntityView

urlpatterns = [
    path('create/', CreateEntityView.as_view(), name='create-entity'),
]
