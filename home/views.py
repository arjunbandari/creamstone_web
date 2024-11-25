from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact 
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is home page")
def about(request):
     return render(request,'about.html')
    #return HttpResponse("this is about page")
def services(request):
     return render(request,'services.html')
    #return HttpResponse("this is  services page")
def payment(request):
    return render(request,'payment.html')
    
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        reason = request.POST.get('reason')

        # Create a new instance of the Contact model
        new_contact = contact(name=name, email=email, address=address, phone=phone, reason=reason)
        new_contact.save()  # Save the new contact to the database

        return HttpResponse('Form submitted successfully')
    else:
        return render(request, 'contact.html')

    #return HttpResponse("this is  contact page")
    def payment(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            order= request.POST.get('order')
            no = request.POST.get('no') 
            form = PaymentForm(request.POST)
            if form.is_valid():
                form.save()  # Save the form data to the database
                return redirect('success')  # Redirect to a success page
            else:
                form = PaymentForm()
                return render(request, 'payment.html', {'form': form})


