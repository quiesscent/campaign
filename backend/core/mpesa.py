from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
import requests
import json
from drf_yasg.utils import swagger_auto_schema
from .serializers import StkPushSerializer
from django.http import JsonResponse
from requests.auth import HTTPBasicAuth
from .models import Transaction
from .credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import logging

logger = logging.getLogger(__name__)

# @csrf_exempt
class StkPushView(APIView):
    @swagger_auto_schema(request_body=StkPushSerializer)
    def post(self, request):
        serializer = StkPushSerializer(data=request.data)
        
        if serializer.is_valid():
            # Extract validated data
            phone_number = serializer.validated_data['phone_number']
            amount = serializer.validated_data['amount']
        
            # Get access token
            access_token = MpesaAccessToken.validated_mpesa_access_token()
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": f"Bearer {access_token}"}

            # Prepare request data
            request_data = {
                "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
                "Password": LipanaMpesaPpassword().decode_password,
                "Timestamp": LipanaMpesaPpassword.get_lipa_time(),
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,
                "PartyA": phone_number,
                "PartyB": LipanaMpesaPpassword.Business_short_code,
                "PhoneNumber": phone_number,
                "CallBackURL": "https://9333-41-209-60-94.ngrok-free.app/api/campaign_callback",
                "AccountReference": "Okiya Campaign",
                "TransactionDesc": "Donation to the OKIYA Foundation"
            }

            # Make STK Push request
            response = requests.post(api_url, json=request_data, headers=headers)
            response_data = response.json()

            # Handle response
            if response_data.get('ResponseCode') == '0':
                return Response({'message': 'STK Push initiated successfully', 'data': response_data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'STK Push failed', 'data': response_data}, status=status.HTTP_400_BAD_REQUEST)
        
        # If data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @method_decorator(csrf_exempt, name='dispatch')
@csrf_exempt
def mpesa_callback(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON
            callback_data = json.loads(request.body)
            logger.info("Callback received: %s", callback_data)

            stk_callback = callback_data['Body']['stkCallback']
            merchant_request_id = stk_callback.get('MerchantRequestID')
            checkout_request_id = stk_callback.get('CheckoutRequestID')
            response_code = stk_callback.get('ResultCode', -1)  # Default to -1 if missing
            response_description = stk_callback.get('ResultDesc', 'No description')

            # Only process and store data if the payment was successful (response_code == 0)
            if response_code == 0:
                callback_metadata = stk_callback.get('CallbackMetadata', {}).get('Item', [])

                # Initialize default values
                amount = 0
                phone_number = ''
                reference = ''
                receipt_number = ''
                transaction_date = ''

                # Extract payment details from metadata
                for item in callback_metadata:
                    if item.get('Name') == 'Amount':
                        amount = item.get('Value', 0)
                    elif item.get('Name') == 'MpesaReceiptNumber':
                        receipt_number = item.get('Value', '')
                    elif item.get('Name') == 'PhoneNumber':
                        phone_number = item.get('Value', '')
                    elif item.get('Name') == 'TransactionDate':
                        transaction_date = item.get('Value', '')      

                Transaction.objects.create(
                        amount=amount,
                        reference=reference,
                )
                logger.info("New transaction created for CheckoutRequestID: %s", checkout_request_id)
                
                return JsonResponse({'message': 'Payment successful and processed'}, status=200)

            else:
                # Log and respond for failed or canceled payments
                logger.warning(
                    "Payment not successful (ResultCode: %d, ResultDesc: %s) for CheckoutRequestID: %s",
                    response_code, response_description, checkout_request_id
                )
                return JsonResponse({
                    'message': 'Payment not successful',
                    'data': {
                        'result_code': response_code,
                        'result_description': response_description
                    }
                }, status=200)

        except KeyError as e:
            logger.error("Missing key in callback data: %s", str(e))
            return JsonResponse({'error': f'Missing key: {str(e)}'}, status=400)
        except json.JSONDecodeError:
            logger.error("Invalid JSON received in callback")
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            logger.error("Unexpected error: %s", str(e))
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# class MpesaCallbackView(APIView):
#     def post(self, request):
#         try:
#             # Parse the incoming JSON
#             callback_data = json.loads(request.body)
#             logger.info("Callback received: %s", callback_data)
#
#             stk_callback = callback_data['Body']['stkCallback']
#             merchant_request_id = stk_callback.get('MerchantRequestID')
#             checkout_request_id = stk_callback.get('CheckoutRequestID')
#             response_code = stk_callback.get('ResultCode', -1)  # Default to -1 if missing
#             response_description = stk_callback.get('ResultDesc', 'No description')
#
#             # Only process and store data if the payment was successful (response_code == 0)
#             if response_code == 0:
#                 callback_metadata = stk_callback.get('CallbackMetadata', {}).get('Item', [])
#
#                 # Initialize default values
#                 amount = 0
#                 phone_number = ''
#                 reference = ''
#                 receipt_number = ''
#                 transaction_date = ''
#
#                 # Extract payment details from metadata
#                 for item in callback_metadata:
#                     if item.get('Name') == 'Amount':
#                         amount = item.get('Value', 0)
#                     elif item.get('Name') == 'MpesaReceiptNumber':
#                         receipt_number = item.get('Value', '')
#                     elif item.get('Name') == 'PhoneNumber':
#                         phone_number = item.get('Value', '')
#                     elif item.get('Name') == 'TransactionDate':
#                         transaction_date = item.get('Value', '')      
#
#                 # Check if the transaction already exists in the database
#                 existing_transaction = Transaction.objects.filter(checkout_request_id=checkout_request_id).first()
#
#                 if existing_transaction:
#                     # Update the transaction with successful payment details
#                     existing_transaction.amount = amount
#                     existing_transaction.phone_number = phone_number
#                     existing_transaction.reference = reference  # Store the reference
#                     existing_transaction.receipt= receipt_number  # Store the receipt number
#                     existing_transaction.save()
#                     logger.info("Transaction updated successfully for CheckoutRequestID: %s", checkout_request_id)
#                 else:
#                     # If the transaction doesn't exist, create a new one for successful payment
#                     Transaction.objects.create(
#                         checkout_request_id=checkout_request_id,
#                         amount=amount,
#                         phone_number=phone_number,
#                         reference=reference,
#                         receipt=receipt_number
#                     )
#                     logger.info("New transaction created for CheckoutRequestID: %s", checkout_request_id)
#
#                 return Response({'message': 'Payment successful and processed'}, status=status.HTTP_200_OK)
#
#             else:
#                 # Log and respond for failed or canceled payments
#                 logger.warning(
#                     "Payment not successful (ResultCode: %d, ResultDesc: %s) for CheckoutRequestID: %s",
#                     response_code, response_description, checkout_request_id
#                 )
#                 return Response({
#                     'message': 'Payment not successful',
#                     'data': {
#                         'result_code': response_code,
#                         'result_description': response_description
#                     }
#                 }, status=status.HTTP_200_OK)
#
#         except KeyError as e:
#             logger.error("Missing key in callback data: %s", str(e))
#             return Response({'error': f'Missing key: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
#         except json.JSONDecodeError:
#             logger.error("Invalid JSON received in callback")
#             return Response({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             logger.error("Unexpected error: %s", str(e))
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

