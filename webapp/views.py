from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from webapp.form import PhotoForm
from webapp.models import Photo, Favorite


class IndexView(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photo'
    queryset = Photo.objects.order_by('created_at')


class PhotoAddView(LoginRequiredMixin, CreateView):
    template_name = 'add_photo.html'
    form_class = PhotoForm

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data.get('photo')
            text = form.cleaned_data.get('text')
            author = request.user
            Photo.objects.create(author=author, photo=photo, text=text)
            return redirect('index')
        return render(request, template_name='add_photo.html', context={'form': form})


class PhotoDetailView(DetailView):
    template_name = 'photo.html'
    model = Photo
    context_object_name = 'photo'


class PhotoEditView(UserPassesTestMixin, UpdateView):
    template_name = 'photo_edit.html'
    form_class = PhotoForm
    model = Photo
    context_object_name = 'photo'

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('change_photo')

    def get_success_url(self):
        return reverse('index')


class PhotoDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'photo_delete.html'
    model = Photo
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('delete_photo')


