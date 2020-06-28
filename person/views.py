import json

from rest_framework import permissions, parsers, views, response, status

from . import serializers, models


class PeopleView(views.APIView):
    parser_classes = (parsers.MultiPartParser,)
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.PersonSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(
            instance=models.Person.objects.all(),
            many=True,
            context={"request": request},
        )
        data = serializer.data
        if data and len(data) > 0:
            return response.Response(data, status=status.HTTP_200_OK, )
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        photo, person = request.data.get('photo', None), request.data.get('person', None)
        person = json.loads(person) if isinstance(person, (str, bytes)) else person
        person['photo'] = photo  # replace photo value with photo file
        serializer = self.serializer_class(data=person)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return response.Response(data={
                'message': 'invalid request data',
                'metadata': ex.args,
            }, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# @renderer_classes((JPEGRenderer,))
# def view_person_photo(request, user_id, format=None):
#     """
#     :param user_id: user ID who's profile image is to be retrieved
#     :param request: HTTP request
#     :param format: how the HTTP base_response should be returned
#     :return: HTTP base_response in format specified by format containing JWT token
#     """
#     image = UserImageUrl.objects.get(user_id=user_id)
#     serializer = UserImageUrlSerializer(instance=image)
#     return Response(data=serializer.data.get('profile'))
