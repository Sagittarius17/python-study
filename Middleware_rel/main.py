# settings.py

MIDDLEWARE = [
    'middleware.testmiddleware1',
    'middleware.testmiddleware2',
    'middleware.testmiddleware3',
]

# middleware.py

class BaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('start', self.middleware_name)
        response = self.get_response(request)
        print('end', self.middleware_name)
        return response


class TestMiddleware1(BaseMiddleware):
    middleware_name = "first middleware"

class TestMiddleware2(BaseMiddleware):
    middleware_name = "second middleware"

class TestMiddleware3(BaseMiddleware):
    middleware_name = "third middleware"
    

# output
    
"""
start first middleware
start second middleware
start third middleware
end third middleware
end second middleware
end first middleware
"""  
