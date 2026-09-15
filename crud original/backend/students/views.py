from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/students/          -> list all students (paginated, filterable)
    POST /api/students/          -> create a new student
    Query params:
      ?search=<text>             -> search first/last name and email
      ?department=<dept>         -> exact filter
      ?year=<1-4>                -> exact filter
      ?ordering=last_name        -> sort (prefix with '-' for descending)
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["department", "year"]
    search_fields = ["first_name", "last_name", "email"]
    ordering_fields = ["first_name", "last_name", "enrollment_date", "year"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET     /api/students/<id>/  -> retrieve a single student
    PUT     /api/students/<id>/  -> full update
    PATCH   /api/students/<id>/  -> partial update
    DELETE  /api/students/<id>/  -> delete
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"message": "Student deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
