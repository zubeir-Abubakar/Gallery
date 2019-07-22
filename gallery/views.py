from django.shortcuts import render
from .models import Image,Location

# Create your views here.
def initial(request):
        locations = Location.objects.all()
        all_images = Image.objects.all()
        return render(request, 'search.html',{"all_images":all_images, "locations": locations})

def search_results(request):
        locations = Location.objects.all()
        if 'searchCategory' in request.GET and request.GET["searchCategory"]:
                search_term = request.GET.get("searchCategory")
                searched_images = Image.search_by_category(search_term)
                message= f"Showing: {search_term} pictures"
                
                return render(request, 'search.html' , {"message":message, "all_images": searched_images, "locations": locations})       #images is a key while searched_images is a value

        else:
                message = "You haven't searched for anything"
                return render(request, 'search.html' , {"message":message}) 

def specific_location(request, location):
        locations = Location.objects.all()
        location_results = Image.filter_location(location)
        return render(request, 'search.html',{"locations": locations, "all_images":location_results})


                

                
        


