import django_filters

from school.models import StudentExtra, Job


class StudentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    college_aggregate = django_filters.CharFilter(
        field_name='college_aggregate', lookup_expr='gte', label='college aggregate greater than')
    school_aggregate = django_filters.CharFilter(
        field_name='school_aggregate', lookup_expr='gte', label='college aggregate greater than')
    hsc_aggregate = django_filters.CharFilter(
        field_name='hsc_aggregate', lookup_expr='gte', label='college aggregate greater than')

    class Meta:
        model = StudentExtra
        fields = ['education', 'university', 'college_aggregate',
                  'school_aggregate', 'hsc_aggregate']


class JobFilter(django_filters.FilterSet):
    salary = django_filters.CharFilter(
        field_name='salary', lookup_expr='gte', label='salary more than')

    class Meta:
        model = Job
        fields = ['salary', 'title']
