from . import models
from django.forms import ModelForm


class Task1Form(ModelForm):
    class Meta:
        model = models.Task1Model
        fields = ['number_of_latent_semantics', 'dataset']


class Task2Form(ModelForm):
    class Meta:
        model = models.Task2Model
        fields = ['number_of_clusters']


class Task3Form(ModelForm):
    class Meta:
        model = models.Task3Model
        fields = ['most_similar_images']


class Task4Form(ModelForm):
    class Meta:
        model = models.Task4Model
        fields = ['classifier', 'dataset', 'kernel', 'number_of_clusters']


class Task5Form(ModelForm):
    class Meta:
        model = models.Task5Model
        fields = ['number_of_layers', 'number_of_hashes_per_layer', 'set_of_vectors', 'query_image',
                  'most_similar_images']


class Task6Form(ModelForm):
    class Meta:
        model = models.Task6Model
        fields = ['query_image','query_image_folder_name', 'most_similar_images', 'relevance_feedback']
