from rest_framework import generics
from rest_framework.response import Response
from .serializers import LinkSerailizer
from rest_framework import status
from .models import Link 
import validators
import random
import string


class LinkShortnerApi(generics.GenericAPIView):
    serializer_class = LinkSerailizer

    def random_ascii(self, input):
        char = random.choice(string.ascii_letters)
        input += char
        return input

    def number_to_decoded_ascii(self, number):
        number = str(number)
        output = ""
        for x in range(0, len(number)):
            output += chr(65+int(number[x*2:x*2+2])%57)
            if x*2+2 >= len(number):
                break
        return output

    def check_new_link_exists(self, new_link):
        if Link.objects.filter(new_link=new_link).count()==0:
            return False
        return True

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        old_link = serializer.validated_data["old_link"]
        if validators.url(old_link):
            try:
                link = Link.objects.create(old_link=old_link)
                decoded_ascii = self.number_to_decoded_ascii(link.pk)
                while self.check_new_link_exists(decoded_ascii):
                    decoded_ascii = self.random_ascii(decoded_ascii)
                link.new_link =  decoded_ascii
                link.save()
                return Response({
                        "message": "ok, new link created",
                        "link": "http://127.0.0.1:8000/api/v1/linkshortener/redirect-page/" + link.new_link
                }, status=status.HTTP_200_OK)
            except:
                return Response({
                        "message": "error, creation failed",
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({
                        "message": "error, url is not valid",
            }, status=status.HTTP_400_BAD_REQUEST)
