from haystack import indexes
from .models import *
class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #, template_name="search/convocatoria_text.txt"
    nombre = indexes.CharField(model_attr='nombre')
    # informacion = indexes.CharField(model_attr='informacion')
    # duracion = indexes.CharField(model_attr='duracion')
    #Categoria = indexes.CharField(model_attr='Categoria')
    #convocatorias = indexes.CharField()

    def get_model(self):
            return Convocatorias

    # def prepare_authors(self, obj):
    #         return [ conv.name for a in obj.convocatorias.all()]
    
    def index_queryset(self, using=None):
            return self.get_model().objects.all()