from rest_framework import generics, permissions
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from django.core.cache import cache

import logging
logger = logging.getLogger('inventory')

# Create a new item
class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        item = serializer.save()
        logger.info(f'Item created: {item}')

# Retrieve a specific item
class ItemDetailView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        cache_key = f'item_{item_id}'
        cached_item = cache.get(cache_key)
        if cached_item:
            logger.info(f"Cache hit for item ID: {item_id}")
            return Response(cached_item)

        item = self.get_object()
        serializer = self.get_serializer(item)
        cache.set(cache_key, serializer.data, timeout=300)  # Cache for 5 minutes
        logger.info(f"Cache set for item ID: {item_id}")
        return Response(serializer.data)
    

# Update an item
class ItemUpdateView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    def perform_update(self, serializer):
        item = serializer.save()
        logger.info(f'Item updated: {item}')
    
# Delete an item
class ItemDeleteView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_destroy(self, instance):
        logger.info(f'Item deleted: {instance}')
        instance.delete()