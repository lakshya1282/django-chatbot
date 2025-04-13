from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

# Configure the Gemini API with your API key
GEMINI_API_KEY = ''
genai.configure(api_key=GEMINI_API_KEY)

def askai(message):
    # Initialize the Gemini model
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # Generate content using Gemini
    response = model.generate_content(message)
    
    # Extract the text from the response
    answer = response.text
    return answer

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = askai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')