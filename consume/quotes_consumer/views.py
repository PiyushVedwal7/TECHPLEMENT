# quotes_consumer/views.py
from django.shortcuts import render
from .models import Quote  # Import your model if needed
from .services import get_random_quote  # Import your service function if needed

def display_quote(request):
    try:
        # Example: Fetching a random quote from a service function or model
        quote = get_random_quote()  # Replace with your actual data retrieval logic
    except Exception as e:
        quote = {'text': 'Error fetching quote', 'author': str(e)}

    return render(request, 'quotes_consumer/quote.html', {'quote': quote})

