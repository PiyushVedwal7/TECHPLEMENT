# quotes_consumer/services.py
import requests

def get_random_quote():
    try:
        response = requests.get('http://127.0.0.1:8000/quotes/random/')  # Replace with your actual API endpoint
        response.raise_for_status()  # Raise HTTPError for bad responses
        quote_data = response.json()  # Assuming API returns JSON data like {'text': 'Quote', 'author': 'Author'}
        return {
            'text': quote_data['text'],
            'author': quote_data['author'],
        }
    except requests.exceptions.RequestException as e:
        # Handle any request exceptions (connection errors, timeouts, etc.)
        return {'text': 'Error fetching quote', 'author': str(e)}
    except KeyError:
        # Handle missing or unexpected data in API response
        return {'text': 'Error: Invalid API response', 'author': ''}
