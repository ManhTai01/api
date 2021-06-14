
from .models import SubmissionJob
from .serializers import SubSerializer, EmailSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, generics
from django.conf import settings
from django.core.mail import send_mail, get_connection
from api_dev.utils.email import Util


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = SubmissionJob.objects.all()
    serializer_class = SubSerializer

    def create(self, request, *args, **kwargs):
        sub1 = SubSerializer(data=request.data)
        if sub1.is_valid():
            sub1.save()
            sub = SubmissionJob.objects.all().order_by('-id').first()
            send_mail('test', 'From' + " " + sub.email + "\n Please Check The Cv in Admin site", settings.EMAIL_HOST_USER,
                      ['lemanhtaictbp@gmail.com'], fail_silently=False)
            print(settings.EMAIL_HOST_USER)
        return Response(sub1.data, status=status.HTTP_201_CREATED)


class EmailView(generics.GenericAPIView):
    serializer_class = EmailSerializer

    def post(self, request):
        print('======================================')
        email = self.serializer_class(data=request.data)
        if email.is_valid():
            send_mail("test", email.data.get(email), settings.EMAIL_HOST_USER,
                      ["lemanhtaictbp@gmail.com"], fail_silently=False)
            print('manhtai')
        test = {'email_body': "tesst", 'to_email': 'lemanhtaictbp.com',
                'email_subject': 'Reset your passsword'}
        Util.send_mail(test)
        return Response('asdasda', status=status.HTTP_200_OK)
