from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from.models import EmployeDetails
from.serializing import EmployeSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
############################# APIView ######################################################


# class testAPIView(APIView):
#     def get(self,request,format=None):
#         data=EmployeDetails.objects.all()
#         serialized=EmployeSerializer(data,many=True)
#         return Response(serialized.data,status=200)

class testAPIView(ListAPIView):
    #queryset=EmployeDetails.objects.all()
    serializer_class=EmployeSerializer
    # custamize quueryset#
    def get_queryset(self):
        qs=EmployeDetails.objects.all()
        name=self.request.GET.get("ename")
        if name is not None:
            qs=qs.filter(ename=name)
        return qs
#class retrive(retriveAPIView):
    #qureyset=EmployeDetails.objects.all()
    #serializer_class=EmployeSerializer
    #lookup_field="id"

# class create(createAPIView):
    #qureyset=EmployeDetails.objects.all()
    #serializer_class=EmployeSerializer

#class updatePatch(updateAPIView):
    #qureyset=EmployeDetails.objects.all()
    #serializer_class=EmployeSerializer
    #lookup_field="id"

#class destroy(destoryAPIView):
    #qureyset=EmployeDetails.objects.all()
    #serializer_class=EmployeSerializer
    #lookup_field="id"
#======== hybrid =========#

#class listCreate(ListCreateAPIView):
# class retriveUpdatePatch(RetriveUpdateAPIView):
# class retriveDestroy(RetriveDestroy):
# class retriveUpdatePatchDestroy(RetriveUpdateDestroyAPIView):

#========= Mixin classes  ========= #

#clasa listmixin(mixin.ListModelMixin)
    # method call= list(self,*args,**kwargs):
#clasa retrievemixin(mixin.RetrieveModelMixin)
    # method call=retrieve(self,*args,**kwargs):
#clasa createmixin(mixin.CreateModelMixin)
    # method call=create(self,*args,**kwargs):
#clasa updatePatchmixin(mixin.UpdateModelMixin)
    #method call=update(self,*args,**kwargs):
    # method call=partial_update(self,*args,**kwargs):
#clasa destroy(mixin.DestroyModelMixin)
    # method call=destroy(self,*args,**kwargs):

# class listcreate(mixin.CreateModelMixin,generic.ListAPIView):
    # queryset=EmployeDetails.objects.all()
    # serializer_class=EmployeSerializer
    # def post(self,request):
    #     return self.create(request,*args)

# class retrieveUpdatePatchDestroy(mixin.UdateModelMxin,mixin.DestroyModelMixin,generic.RetrieveAPIView)
    # queryset=EmployeDetails.objects.all()
    # serializer_class=EmployeSerializer
    # def put(self,request):
    #     return self.update(request,*args)
    # def patch(self,request):
    #     return self.partial_update(request,*args)
    # def delete(self,request):
    #     return self.destroy(request,*args)

 #/////////////////////////////////// viewset ///////////////////////////////////

class viewsetCRUD(ModelViewSet):
    queryset=EmployeDetails.objects.all()
    serializer_class=EmployeSerializer
