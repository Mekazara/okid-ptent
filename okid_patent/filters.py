from django_filters import FilterSet
from .models import Prikaz
from django.db.models import Q
import django_filters


class PrikazFilter(FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter')

    class Meta:
        model = Prikaz
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        queryset = Prikaz.objects.all()
        return queryset.filter(
            Q(number__icontains=value) |
            Q(name__icontains=value) |
            Q(note__icontains=value) |
            Q(file__icontains=value)
        )