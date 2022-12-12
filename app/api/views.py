from rest_framework.response import Response
from rest_framework import viewsets
from core.models import Item
from core.serializers import ItemSerializer
from core.api_utils import FilteredListMixin


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


    def list(self, request, *args, **kwargs):
        series_qs, qs_status = FilteredListMixin.filter_qs(request, self.queryset)
        data = self.serializer_class(series_qs, many=True).data
        
        return Response(data, status=qs_status)