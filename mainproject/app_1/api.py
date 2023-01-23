from rest_framework.decorators import api_view        
from .serializer import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from .models import *
from .serializer import *



# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .serializer import LoginSerializer
# from . import serializers


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)



class ProfileViewApi(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



class StopsApi(viewsets.ModelViewSet):
    queryset = Stops.objects.all()
    serializer_class = StopsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(last_updated_by=user)


class SchoolApi(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by('-updated_at') #for data with shorting
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(last_updated_by=user)


@api_view(('GET',))
def allschooldata(request):

    school_data = School.objects.all().order_by('-updated_at').values()
    data = {
        'school_data':school_data
    }
    return Response(data)


@api_view(('GET',))
def schoolbyschool_id(request, school_id):

    schoolbyschool_id = School.objects.filter(school_id=school_id).values()

    data = {
        'school_data':schoolbyschool_id,

    }
    return Response(data)