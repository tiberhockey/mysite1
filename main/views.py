from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . models import Listing
import ast
import json



# Create your views here.
def home(request):
    return render(request, "main/index.html")

def index2(request):
    listing_object = Listing.objects.all()
    context = {
        "listing_object": listing_object
    }

    return render(request, 'main/index2.html', context)

def index3(request):
    listing_object = Listing.objects.all()
    context = {
        "listing_object": listing_object
    }

    return render(request, 'main/index3.html', context)


def listing(request):
    listings = Listing.objects.all()
    return render(request, "main/listing.html", {'listings': listings})


def test1(request):
    listings = Listing.objects.all()
    return render(request, 'main/test1.html', {'listings':listings})

def test2(request, pk):
    listing_object = Listing.objects.get(id=pk)

    context = {
        'listing_object': listing_object
    }
    return render(request, 'main/test2.html', context)












@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.body)
        webhook_dict_bytes = request.body
        webhook_dict = ast.literal_eval(webhook_dict_bytes.decode('utf-8'))  # convert byte data to normal dict


        #Save models
        """category_instance = Category.objects.get(id=pattern_instance_id)
        new_listing_objects = Photo(category=category_instance,
                                    symbol=webhook_dict['symbol'],
                                    image=webhook_dict['pic_directory'],
                                    pattern=webhook_dict['pattern'],
                                    timeframe=webhook_dict['TimeFrame'],
                                    pattern_date=webhook_dict['Date']
                                    )

        new_pattern_objects.save()"""

        new_listing_objects = Listing(
            listing_uls=webhook_dict["listing_uls"],
            listing_type=webhook_dict["listing_type"],
            listing_price=webhook_dict["listing_price"],
            listing_address=webhook_dict["listing_address"],
            listing_piece=webhook_dict["listing_piece"],
            listing_chambre=webhook_dict["listing_chambre"],
            listing_nb_salle_de_bain=webhook_dict["listing_nb_salle_de_bain"],
            listing_dimensions=webhook_dict["listing_dimensions"],
            listing_year=webhook_dict["listing_year"],
            listing_energetique=webhook_dict["listing_energetique"],
            listing_fenestration=webhook_dict["listing_fenestration"],
            listing_revetement=webhook_dict["listing_revetement"],
            listing_revetement_toiture=webhook_dict["listing_revetement_toiture"],
            listing_laveuse_secheuse=webhook_dict["listing_laveuse_secheuse"],
            listing_garage=webhook_dict["listing_garage"],
            listing_armoire=webhook_dict["listing_armoire"],
            listing_salle_de_bain=webhook_dict["listing_salle_de_bain"],
            listing_sous_sol=webhook_dict["listing_sous_sol"],
            listing_renovation=webhook_dict["listing_renovation"],
            listing_topographie=webhook_dict["listing_topographie"],
            listing_vue=webhook_dict["listing_vue"],
            listing_alle=webhook_dict["listing_alle"],
            listing_stationnement=webhook_dict["listing_stationnement"],
            listing_chauffage=webhook_dict["listing_chauffage"],
            listing_energie=webhook_dict["listing_energie"],
            listing_desc=webhook_dict["listing_desc"]
        )
        new_listing_objects.save()

        return render(request, "main/index.html")