from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import requests
from django.conf import settings
from django.http import JsonResponse
import urllib.parse

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


def lock_dashboard(request):
    return render(request, 'pages/lock_dashboard.html')

def send_message_to_esp32(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        esp32_ip = 'http://10.0.175.67/receive-message'  # Replace with the actual IP address and endpoint

        try:
            # Send the message to the ESP32
            response = requests.post(esp32_ip, data={'message': message})
            if response.status_code == 200:
                return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Failed to send message to ESP32.'})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

'''
def geocode_address(request):
    address = request.GET.get('address')
    if not address:
        return JsonResponse({'error': 'No address provided'}, status=400)

    # address = urllib.parse.quote(address)
    # api_key = settings.GOOGLE_MAPS_API_KEY
    # url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    
    address = "No. 85, Section 3, Keelung Rd, Da’an District, Taipei City, 107"
    encoded_address = urllib.parse.quote(address)
    url = f"/geocode/?address={encoded_address}"

    
    response = requests.get(url)
    data = response.json()
    print(data)

    if data['status'] == 'OK':
        # 提取經緯度
        location = data['results'][0]['geometry']['location']
        return JsonResponse(location)
    else:
        return JsonResponse({'error': 'Failed to geocode address'}, status=400)
'''