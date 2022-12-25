from django.urls import path

from item.views import CreateListEntityView

urlpatterns = [
    path('', CreateListEntityView.as_view(), name='create-entity'),
]
