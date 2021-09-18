from django.shortcuts import render, HttpResponse,HttpResponseRedirect,get_object_or_404,redirect
from django.urls import reverse
from django.template.loader import get_template
import os
from xhtml2pdf import pisa

from List.models import Employee,Ta_Da

def index(request):

    if(request.method=="POST"):
        t_cost=0
        l_cost=0
        i_cost=0        
        date = request.POST["date"]
        name = request.POST["name"]
        t_cost = request.POST["t_cost"]
        l_cost = request.POST["l_cost"]
        i_cost = request.POST["i_cost"]
        tl_cost = float(t_cost)+ float(l_cost)+ float(i_cost)
        status = request.POST["status"]
        instance = Ta_Da(date=date,name=name,travel_cost=t_cost,lunch_cost=l_cost,instrument_cost=i_cost,total_cost=tl_cost,Paid=status)
        instance.save()
        return HttpResponseRedirect(reverse('List:show'))
    names = Employee.objects.all()
    diction ={'names':names}
    return render(request,'List/index.html',context=diction)

def show(request):
    tadas= Ta_Da.objects.all().order_by('-Paid','-date')

    diction ={'tadas':tadas}
    return render(request,'List/show.html',context=diction)

def change(request, pk):
    item = get_object_or_404(Ta_Da, pk=pk)
    item.Paid="paid"
    item.save()
    print(item)

    return redirect("List:show")

def render_pdf_view(request):
    tadas= Ta_Da.objects.all().order_by('-Paid','-date')
    template_path = 'List/pdf.html'
    context = {'tadas': tadas}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="TA_DA_List.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response