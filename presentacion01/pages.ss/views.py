from django.http import HttpResponse

def homePageView(request):
	documento = """
    <br>
    <h1>Hola! este e mi proyecto</h1>
    <br>
    """
    return HttpResponse(documento);
	