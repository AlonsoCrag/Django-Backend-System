from rest_framework.serializers import ModelSerializer
from Accounts.models import Account

# Pass data to serialize, like QuerySets from models
class SerializeData(ModelSerializer):
    class Meta:
        model = Account
        fields = ["Username", "Email","Password", "Salt"]
