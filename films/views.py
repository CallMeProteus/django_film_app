from audioop import reverse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Film


class FilmBaseView(View):
    model = Film
    fields = '__all__'
    success_url = reverse_lazy('films:all')



class FilmListView(FilmBaseView, ListView):
     """ view to list all films, use the film_
    list variable in the remplate to access all film objects """
   
   
class FilmDetailView(FilmBaseView, DetailView):
    """ View to list details from one film 
    use film variable in template to acess specific film here 
    and in the views bellow """

class FilmCreateView(FilmBaseView, CreateView):
    """ View to update film """


   
class FilmUpdateView(FilmBaseView, UpdateView):
    """ View to update film """


   
class FilmDeleteView(FilmBaseView, DeleteView):
    """View to delete a film """