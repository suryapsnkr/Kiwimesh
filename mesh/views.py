from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from mesh.serializers import CreateNoteSerializer, NoteSerializer
from mesh.models import Note
from rest_framework.response import Response

# Create your views here.

@method_decorator(csrf_protect, name='dispatch')
class Notes(APIView):
    def get(self, request, format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Message': 'Note Added Successfully'})

@method_decorator(csrf_protect, name='dispatch')
class GetNote(APIView):
    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        if pk<=0:
            return Response({"Message": "Negative OR Zero Indexing is Not Supported"})
        else:    
            notes = Note.objects.filter(id = pk)
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Message': 'Note Updated Successfully'})

@method_decorator(csrf_protect, name='dispatch')
class Query(APIView):
    def get(self, request, title):
        query= Note.objects.filter(title__icontains = title)
        serializer = NoteSerializer(query, many = True)
        return Response(serializer.data)
