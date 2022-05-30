class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization")
    
    def __call__(self, request):
        print("This is Before View")
        response = self.get_response(request)
        print("This is After view")
        return response