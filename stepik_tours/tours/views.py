from django.shortcuts import render
# from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views import View

# def custom_handler404(request, exception):
#     return HttpResponseNotFound("Нет такой страницы")


# def custom_handler500(request):
#      return HttpResponseServerError("Ошибка на сервере")


class MainView(View):

    def get(self, request):

        count = range(6)
        ii = "iterator"
        context = {
            'count': count,
            'ii': ii,
        }
        return render(request, 'list_tours.html', context=context)


dep_data = {
    'Novosibirsk': "departure.html",
}


def DepartureView(request, departure):
    dep_res = dep_data.get(departure)
    return render(request, dep_res)


# tour_data = {
#     1: "tour.html", 2: "tour.html"
# }


def TourView(request, id):
    # tour = tour_data.get(id)
    return render(request, 'tour.html')
