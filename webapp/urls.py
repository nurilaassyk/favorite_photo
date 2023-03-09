from django.urls import path

from webapp.views import IndexView, PhotoAddView, PhotoDetailView, PhotoEditView, PhotoDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/add/', PhotoAddView.as_view(), name='add_photo'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail'),
    path('photo/<int:pk>/edit/', PhotoEditView.as_view(), name='edit'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),
    # path('photo/<int:pk>/to-favorite/', FavoriteView.as_view(), name='to_favorite'),
]
