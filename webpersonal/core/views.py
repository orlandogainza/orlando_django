from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    html_response = "<h1>Hola Crayola</h1>"
    for i in range(5):
        html_response += "<h2>crayolita</h2>"
    return HttpResponse(html_response)