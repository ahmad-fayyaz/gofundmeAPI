# apify_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apify_client import ApifyClient
from .serializers import FundraiserSerializer

class ApifyDataView(APIView):
    def get(self, request):
        # Initialize the ApifyClient with your API token
        client = ApifyClient("apify_api_hr8QQoPaTDPbApr4qdOKBTX2R9eoFp4sSCjq")

        # Prepare the Actor input
        run_input = {
            'query': 'mutual aid',
            'limit': 6,  # This limit can be dynamic or based on user input
        }

        # Run the Actor and wait for it to finish
        run = client.actor("RDZ33qDF65SRiTnxx").call(run_input=run_input)

        # Fetch Actor results from the run's dataset
        data = []
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            # Map the fields from Apify API response to match the serializer fields
            fundraiser_data = {
                'url': item.get('url', ''),
                'fundname': item.get('fundname', ''),
                'balance': item.get('balance', 0),
                'goal_progress': item.get('goal_progress', 0),
                'amount_to_goal': item.get('amount_to_goal', 0),
                'username': item.get('username', ''),
                'currencycode': item.get('currencycode', ''),
                'donation_count_full': item.get('donation_count_full', 0),
                'thumb_img_url': item.get('thumb_img_url', ''),
                'objectID': item.get('objectID', '')
            }
            data.append(fundraiser_data)

            # Stop adding more items if we have reached the limit
            if len(data) >= run_input['limit']:
                break

        # Serialize the data
        serializer = FundraiserSerializer(data=data, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)