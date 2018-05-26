#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views import View





class Index(View):
    template_name = 'index.html'
    def get(self, request,  *args, **kwargs):
        #dictionary = json.dumps(response)
        context = {'message':'ooooppppppp'}
        return render(request, self.template_name, context)

    def post(self, request,  *args, **kwargs):
        #dictionary = json.dumps(response)
        return HttpResponse()