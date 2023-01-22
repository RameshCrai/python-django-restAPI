from django.http import HttpResponse, JsonResponse


def home_page(request):
    friends = [
        'ramesh',
        'sandesh',
        'john',
        'bikram'
    ]
    return JsonResponse(friends, safe=False)
