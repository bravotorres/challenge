import logging
import os

from django.core.files.storage import default_storage
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api import models


# Log System
logger = logging.getLogger(__name__)


class Album(APIView):
    def __init__(self):
        self.response = {
            'response_body': None,
            'message': 'Data not found.',
            'status': status.HTTP_204_NO_CONTENT,
        }

    def get(self, request):

        try:
            albums = models.Album.objects.all()

            self.response['response_body'] = albums

            return Response(self.response, status=status.HTTP_200_OK)
        except Exception as e:
            logger.info(e)
            return Response(self.response, status=status.HTTP_400_BAD_REQUEST)


class Photo(APIView):
    # parser_classes = (FileUploadParser,)

    def __init__(self):
        self.response = {
            'response_body': None,
            'message': 'Data not found.',
            'status': status.HTTP_204_NO_CONTENT,
        }

        self.storage_folder = 'photos'
        self.base_name = '{}'.format(timezone.now().strftime("%F_%H%M%S"))

    def get(self, request):

        try:
            photos = models.Photo.objects.all()

            self.response['response_body'] = photos
            self.response['status'] = status.HTTP_205_RESET_CONTENT

            return Response(self.response, status=self.response['status'])
        except Exception as e:
            logger.info(e)
            return Response(self.response, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):

        try:
            uploaded_file = request.data['uploaded_file']

            # up_file = request.FILES['file']
            file_name = uploaded_file.name.split('.')
            ext = file_name.pop()
            img_name = ''.join(file_name)
            full_name = "{}_{}.{}".format(img_name, self.base_name, ext)

            path = default_storage.path(os.path.join(self.storage_folder, full_name))

            destination = open(path, 'wb+')

            for chunk in uploaded_file.chunks():
                destination.write(chunk)

            destination.close()

            # Save entry in database...

            return Response("Imágen Guardada exitosamente.", status=status.HTTP_200_OK)
        except Exception as e:
            self.detail['err'].append(e.args[0])
            logger.warning(e)
            logger.info(e)
            return Response(self.detail, status=status.HTTP_400_BAD_REQUEST)

            photos = models.Photo.objects.all()

            self.response['response_body'] = photos
            self.response['status'] = status.HTTP_205_RESET_CONTENT

            return Response(self.response, status=self.response['status'])
