from django.shortcuts import render
from .models import Item
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

# Load shop information from configuration file
shop_info_path = os.path.join(os.path.dirname(__file__), '..', 'shop_info.json')
with open(shop_info_path) as f:
    shop_info = json.load(f)


def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

def business_info(request):
    return render(request, 'items/business_info.html')


@csrf_exempt
def manychat_webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data['messages'][0]['text']
        chatgpt_response = get_chatgpt_response(user_message)

        # Check for specific keywords to provide shop information
        if "address" in user_message.lower():
            response_text = f"Our shop is located at {shop_info['address']}."
        elif "hours" in user_message.lower():
            response_text = f"Our business hours are {shop_info['hours']}."
        elif "phone" in user_message.lower():
            response_text = f"You can contact us at {shop_info['phone']}."
        elif "email" in user_message.lower():
            response_text = f"You can email us at {shop_info['email']}."
        elif "return policy" in user_message.lower():
            response_text = shop_info['return_policy']
        elif "shipping" in user_message.lower():
            response_text = shop_info['shipping_info']
        elif "special offers" in user_message.lower():
            response_text = shop_info['special_offers']
        else:
            response_text = chatgpt_response

        response_data = {
            'messages': [
                {'text': response_text}
            ]
        }
        return JsonResponse(response_data)


def get_chatgpt_response(message):
    openai.api_key = 'your-openai-api-key'
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=150
    )
    return response.choices[0].text.strip()