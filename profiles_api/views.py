from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        an_apiview = [
            "Uses HTTP methods as function (GET, POST, PATH, PUT, DELETE)"
            "Is Similar to traditional django View.",
            "Gives you the most control over your Application logic.",
            "Is mapped manually to URLs.",
        ]
        return Response({'message' : 'Hello!', 'an_apiview': an_apiview})
    

