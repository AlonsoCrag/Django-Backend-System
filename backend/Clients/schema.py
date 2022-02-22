from multiprocessing.connection import Client
import graphene
from graphene_django import DjangoObjectType
from Accounts.models import Account

class ClientType(DjangoObjectType):
    class Meta:
        model = Account
        field = ('Username', 'Email', 'Picture')


class Query(graphene.ObjectType):
    allUsers = graphene.List(ClientType)
    unicUser = graphene.Field(ClientType, Username=graphene.String())

    def resolve_allUsers(root, info, **kwargs):
        return Account.objects.all()

    def resolve_unicUser(root, info, **kwargs):
        return Account.objects.get(Username=kwargs["Username"])

schema = graphene.Schema(query=Query)