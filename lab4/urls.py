from django.urls import path

from .views import lab4_create_view, lab4_select_view, lab4_details_view


app_name = 'lab4'
urlpatterns = [
    path('create/', lab4_create_view, name='create'),
    path('retrieve/', lab4_select_view, name='retrieve'),
    path('details/<int:_id>/', lab4_details_view, name='details'),
]

