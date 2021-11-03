from rest_framework import serializers 
from . import models

class PayRecordSerializer(serializers.ModelSerializer):
    class Meta: ## Properties of the class (think of right clicking on image and pressing Properties
        model = models.PayRecord 
        fields = "__all__"
        extra_kwargs = {
            'transaction_id': {
                'read_only': True
            }
        }


class BusinessesSerializer(serializers.ModelSerializer):

    class Meta: 
        model = models.Businesses
        fields = "__all__"

## After serializing something, we need to make sure it is valid 