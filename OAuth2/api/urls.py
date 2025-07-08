from django.urls import path
from .views import ExampleApiView, ReadScopeOnlyView, home

urlpatterns = [
    path('', home, name='api_home'),  
    path('example/', ExampleApiView.as_view(), name='example'),
    path('read-only/', ReadScopeOnlyView.as_view(), name='read_only'),
]