from django.urls import path
from . import views
from Clients.views import Clients
from graphene_django.views import GraphQLView
from Clients.schema import schema
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html')),
    path('api/v1/register/', views.Register, name="Route to register users"),
    path('api/v1/login/', views.Login, name="Route to log users"),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))
]