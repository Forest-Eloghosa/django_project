from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
        html = """
        <html>
            <head>
            <title>Hello</title>
            </head>
            <body>
                <h1>Hello, world!</h1>
                <p><a href="/about/">About page</a></p>
            </body>
        </html>
        """
        return HttpResponse(html)