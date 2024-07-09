# apify_app/serializers.py
from rest_framework import serializers

class FundraiserSerializer(serializers.Serializer):
    url = serializers.CharField()
    fundname = serializers.CharField()
    balance = serializers.FloatField()
    goal_progress = serializers.FloatField()
    amount_to_goal = serializers.FloatField(allow_null=True)
    username = serializers.CharField()
    currencycode = serializers.CharField()
    donation_count_full = serializers.IntegerField()
    thumb_img_url = serializers.URLField()
    objectID = serializers.CharField()


# random 
