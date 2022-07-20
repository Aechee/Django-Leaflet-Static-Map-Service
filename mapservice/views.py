from urllib import response
from django.http import HttpResponse
import staticmaps
from io import StringIO



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def getMap(request):
    context = staticmaps.Context()
    context.set_tile_provider(staticmaps.tile_provider_OSM)

    frankfurt = staticmaps.create_latlng(50.110644, 8.682092)   
    newyork = staticmaps.create_latlng(40.712728, -74.006015)

    context.add_object(staticmaps.Line([frankfurt, newyork], color=staticmaps.BLUE, width=4))
    context.add_object(staticmaps.Marker(frankfurt, color=staticmaps.GREEN, size=12))
    context.add_object(staticmaps.Marker(newyork, color=staticmaps.RED, size=12))

    # render non-anti-aliased png
    image = context.render_pillow(800, 500)
    resposne = HttpResponse(content_type="image/png")
    image.save(resposne,'png')

    return resposne
