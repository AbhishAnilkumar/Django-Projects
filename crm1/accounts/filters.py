import django_filters
from django_filters import DateFilter, CharFilter


from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')#greater than or equal)
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')#less than or equal)
    class Meta: #Meta is used to customize a models behavior
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created',]
#used __all__ to get all the fields and exclude to not render certain fields


#This page is similar to forms.py