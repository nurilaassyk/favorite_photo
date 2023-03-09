from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Favorite, Photo


class FavoriteCreateView(APIView):
    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        user_id = request.data.get('user_id')
        user = User.objects.get(pk=user_id)
        favorite, created = Favorite.objects.get_or_create(user=user, photo=photo)
        if created:
            return Response(data={'detail': 'Добавлено'}, status=200)
        favorite.delete()
        return Response(data={'detail': 'Удалено'}, status=200)


# class CommentView(FormView):
#     def post(self, request, *args, **kwargs):
#         photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
#         user_id = request.data.get('user_id')
#         user = User.objects.get(pk=user_id)
#         form = self.get_form_class()(request.POST)
#         if form.is_valid():
#             text = form.cleaned_data.get('text')
#             Comment.objects.create(user=user, photo=photo, text=text)
#         return Response(status=200)

