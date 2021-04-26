import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    body = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Student
        fields = '__all__'


