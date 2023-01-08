from django.shortcuts import render, redirect
from django.views import View
from .forms import CustumerForm
from django.http import HttpResponse
from .models import Custumor

# Create your views here.
class CustumerView(View):
    def get(self, request):
        form = CustumerForm()
        template_name = 'CRUD-APP/customer_form.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request):
        form = CustumerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_url')
        return HttpResponse("Invalid DATA!!!")

class ShowView(View):
    def get(self, request):
        obj = Custumor.objects.all()
        template_name = 'CRUD_APP/customer_list.html'
        context = {'data': obj}
        return render(request, template_name, context)

class UpdateView(View):
    def get(self, request, pk):
        obj = Custumor.objects.get(c_id=pk)
        form = CustumerForm(instance=obj)
        template_name = 'CRUD_APP/customer_form.html'
        context = {'form':form}
        return render(request, template_name, context)

    def post(self, request, pk):
        obj = Custumor.objects.get(c_id=pk)
        form = CustumerForm(instance=obj)
        if request.method == "POST":
            form = CustumerForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('display_url')

        template_name = "CRUD_APP/customer_form.html"
        context = {'form': form}
        return render(request, template_name, context)

class DeleteView(View):
    def get(self, request, pk):
        obj = Custumor.objects.get(c_id=pk)
        obj.delete()
        return redirect('display_url')



