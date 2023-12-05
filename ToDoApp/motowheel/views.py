import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



def index(request):

    data = {
        'map':       ['|[]‾‾[]‾‾[]‾‾[]‾‾[]‾‾[]‾‾[]‾‾|',
                    '|  []  []  []  []  []  []  []|',
                    '|[]  []  []  []  []  []  []  |',
                    '|__[]__\|__[]______[]__\|__[]|',
                    '|                        Ԑ3  →',
                    '| __/‾‾\__             Ԑ3Ԑ3Ԑ3→',
                    '| /о\__/о\   ||      О Ԑ3Ԑ3Ԑ3|',
                    '| __/‾‾\__ ++||++   ОО ԐԐ||Ԑ3|',
                    '| /о\__/о\   ||          ||  |',
                    '|     Ԑ3           О|‾‾‾‾|О  |',
                    '|   Ԑ3Ԑ3Ԑ3         О|    |О  |',
                    '|   Ԑ3Ԑ3Ԑ3         О|____|О  |',
                    '←   ԐԐ||Ԑ3    1       О ОО   |',
                    '|_____||_____________________|']
    }
    return render(request, "motowheel/index.html", context=data)
