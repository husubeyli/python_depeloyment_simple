
from rest_framework.views import APIView
from rest_framework.response import Response
from main.api.serializers import AccountCreateSerializer, AccountSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from main.models import Account



class AccountAPIView(APIView):
    queryset = Account.objects.all()
    
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        serilizer = AccountSerializer(accounts, many=True, context = {'request' : request})
        return Response(data=serilizer.data, status=HTTP_200_OK)


    def post(self, request, *args, **kwargs):
            recipe_data = request.data
            serializer = AccountCreateSerializer(data=recipe_data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)