from django.http import HttpResponse

def docker(request):
    return HttpResponse("<h2>What is Docker?<h2/><h2> Docker makes development efficient and predicatable Docker takes away repetitive, mundane configuration tasks and is used throughout the development lifecycle for fast, easy and portable application development desktop and cloud.<h2/> <h2>Docker's comprehensive end to end platform includes UIs, CLIs, APIs and security that are engineered to work together across the entire application delivery lifecycle<h2/>")   