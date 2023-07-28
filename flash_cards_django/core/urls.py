from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('deck/', views.deck_create, name='deck-create'),
    path('deck/<int:id>/', views.deck_edit, name='deck-edit'),
    path('card/', views.card_create, name='card-create'),
    path('card/<int:id>/', views.card_edit, name='card-edit'),
]
