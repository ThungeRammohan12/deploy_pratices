from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

# List all contacts and create a new one
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# Retrieve, update, or delete a specific contact
class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
