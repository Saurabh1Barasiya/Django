from django.shortcuts import HttpResponse
class Brother:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Brother Initialization")
    
    def __call__(self, request):
        print("This is Brother Before View")
        response = self.get_response(request)
        print("This is Brother After view")
        return response

class Father:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Father Initialization")
    
    def __call__(self, request):
        print("This is Father Before View")
        response = self.get_response(request)
        # response = HttpResponse("Nikal lo")
        print("This is Father After view")
        return response

class Mother:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Mother Initialization")
    
    def __call__(self, request):
        print("This is Mother Before View")
        response = self.get_response(request)
        print("This is Mother After view")
        return response