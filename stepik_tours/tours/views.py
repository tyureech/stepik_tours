from random import sample

from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views import View

from . import data


def custom_handler404(request, exception):
    return HttpResponseNotFound("Нет такой страницы")


def custom_handler500(request):
    return HttpResponseServerError("Ошибка на сервере")


class MainView(View):

    def get(self, request):

        rand_tours = {}
        list_rand_tours_id = sample(list(data.tours), 6)

        for x in list_rand_tours_id:
            rand_tours[x] = data.tours[x]

        context = {
            'tours': rand_tours,
        }

        return render(request, 'index.html', context=context)


class DepartureView(View):

    def get(self, request, departure):

        n = 0
        tours_dep = {}
        country = data.departures[departure].split()
        end_of_word = ''
        price = []
        night = []

        for i, j in data.tours.items():
            if j["departure"] == departure:
                tours_dep[n] = j
                price.append(j["price"])
                night.append(j["nights"])
                tours_dep[n]['id_tour'] = i
                n += 1

        price.sort()
        night.sort()

        if n != 1 and (n >= 2 and n <= 4):
            end_of_word = 'а'
        else:
            end_of_word = 'ов'

        context = {
            'tours_dep': tours_dep,
            'n': n,
            'country': country[1],
            'end_of_word': end_of_word,
            'min_price': price[0],
            'max_price': price[-1],
            'min_night': night[0],
            'max_night': night[-1]
        }
        return render(request, 'departure.html', context=context)


class TourView(View):

    def get(self, request, id):

        tour = data.tours.get(id)
        star = '★' * int(tour["stars"])
        context = {
            'tour': tour,
            'star': star,

        }
        return render(request, 'tour.html', context=context)

