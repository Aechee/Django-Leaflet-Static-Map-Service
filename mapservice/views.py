from urllib import response
from django.http import HttpResponse
import staticmaps
from io import StringIO



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def getMap(request):
    context = staticmaps.Context()
    context.set_tile_provider(staticmaps.tile_provider_OSM)
    context.set_zoom(15)

    # Creating Single Lat Long to Add on map
    markerLocation = staticmaps.create_latlng(33.678421509327215, 73.0483424974427)   
    polygonLocation = staticmaps.Area([staticmaps.create_latlng(33.68356396446586, 73.04902914294371),
    staticmaps.create_latlng(33.688599670247875, 73.07246954084945),staticmaps.create_latlng(33.67781864409684, 73.07775428510458),
    staticmaps.create_latlng(33.68356396446586, 73.04902914294371)],
        fill_color=staticmaps.parse_color("#00FF003F"),
        width=2,
        color=staticmaps.BLUE)
    
    # Adding polygon and marker on map
    context.add_object(polygonLocation)
    context.add_object(staticmaps.Marker(markerLocation, color=staticmaps.GREEN, size=12))
    
    
    # rendering the created image in django response as image
    image = context.render_pillow(800, 500)
    resposne = HttpResponse(content_type="image/png")
    image.save(resposne,'png')

    return resposne
