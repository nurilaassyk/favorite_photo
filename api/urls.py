from django.urls import path

from api.views import FavoriteCreateView

urlpatterns = [
    path('photo/<int:pk>/to-favorite/', FavoriteCreateView.as_view(), name='favorite'),
]
