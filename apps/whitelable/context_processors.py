# myapp/context_processors.py
from .utils import get_user_data
# from django.core.cache import cache

def global_vars(request):
    # Attempt to fetch the value from the cache
    # data = cache.get('global_var')
    data =get_user_data(request)
    # print(data)
    # If the value was not cached, compute it and cache it
    # if data is None:
        # data =get_user_data(request)
        # print(data)
        # Cache these variables for 10 minutes (or any appropriate duration)
        # cache.set('global_var', data, 600) # Cache duration in seconds

    # Return the variables (whether they were retrieved from cache or just set)
    if request.user.is_authenticated:
        return data
    else:
        return {
            "body":"login"
        }
        
