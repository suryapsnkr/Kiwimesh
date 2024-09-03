from rest_framework import serializers
from mesh.models import Note

class CreateNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'body']

    def create(self, validated_data):
        note = Note(
            title = validated_data['title'],
            body = validated_data['body'],
        )
        note.save()
        return note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'body']