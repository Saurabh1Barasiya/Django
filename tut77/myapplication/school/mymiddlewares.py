from django.shortcuts import HttpResponse
class UnderConstructionMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # if request.path == '/under-construction/':
        #     return HttpResponse('Under Construction')
        # return self.get_response(request)
        print("Call from middleware")
        # response = self.get_response(request)
        response = HttpResponse("This side is Under Construction") # <-- jab site sahi ho jaye to isko comment kar do . and upper wali line ko uncomment kar do.

        return response