from django.shortcuts import render, redirect
from crud.models import Bank,Customer
from crud.forms import bankForm,customerForm
from django.contrib.auth.decorators import login_required


def update_customer(request, pk):

    data = Customer.objects.get(id=pk)
    form = customerForm(instance=data)
    if request.method == 'POST':
        form = customerForm(request.POST, instance=data)
        if form.is_valid():
            #form.save()
            c_obj = Customer()
            c_obj.id = pk
            c_obj.name = form.cleaned_data['name']
            c_obj.bank_id = form.cleaned_data['bank']
            c_obj.email = form.cleaned_data['email']
            c_obj.save()
            return redirect('customer_index')
    return render(request, 'customer/update.html', {'form': form})


def createCustomer(request):

    form = customerForm()

    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            #form.save()
            c_obj = Customer()
            c_obj.name = form.cleaned_data['name']
            c_obj.bank_id = request.POST['bank']
            c_obj.email = form.cleaned_data['email']
            c_obj.save()
            return redirect('customer_index')
    return render(request, 'customer/create.html', {'form':form})


def customerIndex(request):

    data = Customer.objects.all()

    return render(request, 'customer/index.html',{'data':data})




def view(request, pk):

    data = Bank.objects.get(id=pk)

    return render(request, 'view.html', {'data':data})

def delete(request, pk):

    data = Bank.objects.get(id=pk)
    data.delete()
    #delete from  bank where id = pk
    return redirect('index')

def update(request, pk):

    data = Bank.objects.get(id=pk)

    #select * from  bank where id=pk
    form = bankForm(instance=data)

    if request.method == 'POST':
        form = bankForm(request.POST, instance=data)
        if form.is_valid():
            # form.save()
            bank = Bank()
            bank.id = pk
            bank.name = form.cleaned_data['name']
            bank.email = form.cleaned_data['email']
            bank.address = form.cleaned_data['address']
            bank.save()
            return redirect('index')

    return render(request, 'update.html', {'form': form})



def create(request):

    form = bankForm()

    if request.method == 'POST':
        form = bankForm(request.POST)
        if form.is_valid():
            #form.save()
            bank = Bank()
            bank.name = form.cleaned_data['email'].split('@')[0]
            bank.email = form.cleaned_data['email']
            bank.address = form.cleaned_data['address']
            bank.save()
            return redirect('index')
    return render(request, 'create.html', {'form':form})

@login_required(login_url='/signin')
def index(request):

    data = Bank.objects.all()
    #data = Bank.objects.raw("select * from bank")

    #select * from bank

    return render(request, 'index.html',{'data':data})

