from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from . import models 
from . import serializers
# Create your views here.

class MyFirstFreakinView(generics.ListCreateAPIView):

    serializer_class = serializers.PayRecordSerializer
    queryset = models.PayRecord.objects.all()
    
# # CTRL + / to comment multiple lines of code 

#     def get(self, request): 
#         employees = models.PayRecord.objects.all()
#         serializer = self.serializer_class(employees, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                     'message':'Pay Record Saved!'
#                 })

#     def put(self, request):
#         pass 

#     def delete(self, request):
#         pass


class EditRecordView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.PayRecordSerializer
    lookup_url_kwarg = 'pk'
    queryset = models.PayRecord.objects.all()
#     def get_object(self, pk):
#         try: 
#             return models.PayRecord.objects.get(pk=pk)

#         except models.PayRecord.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         serializer = self.serializer_class(self.get_object(pk))
#         return Response(serializer.data)

#     def put(self, request, pk):
#         record = self.get_object(pk)
#         serializer = self.serializer_class(record, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#     def delete(self, request, pk):
#         record = self.get_object(pk)
#         record.delete()
#         return Response('Employee Deleted')


# class SecondFreakinView(APIView): 
#     def get(self, request): 
#         business = models.Businesses.objects.all()
#         serializer = serializers.BusinessesSerializer(business, many = True)
    
#     def post(self, request):
#         pass

#     def put(self, request):
#         pass

#     def delete(self, request):
#         pass

