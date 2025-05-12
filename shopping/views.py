from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import ShoppingList, Item
from django.utils.text import slugify

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



def home(request):
    return render(request, 'shopping/home.html')

def create_list(request):
    new_list = ShoppingList.objects.create()
    return redirect('view_list', list_uuid=new_list.uuid)

def view_list(request, list_uuid):
    shopping_list = get_object_or_404(ShoppingList, uuid=list_uuid)

    if request.method == 'POST':
        item_name = request.POST.get('item')
        if item_name:
            new_item = Item.objects.create(list=shopping_list, name=item_name)

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f'shopping_{list_uuid}',
                {
                    'type': 'shopping_message',
                    'message': new_item.name
                }
            )

        return redirect('view_list', list_uuid=list_uuid)


    items = shopping_list.items.order_by('-added_at')
    return render(request, 'shopping/view_list.html', {'shopping_list': shopping_list, 'items': items, 'list_uuid': list_uuid})


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.is_bought = not item.is_bought
    item.save()
    return redirect('view_list', list_uuid=item.list.uuid)

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    list_uuid = item.list.uuid
    item.delete()
    return redirect('view_list', list_uuid=list_uuid)


