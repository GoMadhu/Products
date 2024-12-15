from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Products_List
from django.contrib import messages

def home(request):
    
    productlist = Products_List.objects.order_by('-id')
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        checklist = request.POST.get('check')
        if checklist:
            post = Products_List(
                product_name=name,
                product_price = price,
                product_status=True,
            )
            post.save()
            messages.success(request,'Product Created Successfully', extra_tags='success')
            return redirect('home')
        else:
            post = Products_List(
                product_name=name,
                product_price = price,
                product_status=False
            )
            post.save()
            messages.success(request,'Product Created Successfully', extra_tags='success')
            return redirect('home')
    context = {
        'products':productlist,
    }
    return render(request,'home.html', context)

def update(request, id):
    print(id,'jjd')
    
    if request.method == "POST" and 'update' in request.POST:
        name = request.POST.get('uname')
        price = request.POST.get('uprice')
        checklist1 = request.POST.get('ucheck1')
        if checklist1:
            Products_List.objects.filter(id=id).update(
                product_name = name,
                product_price = price, 
                product_status = True
            )
            messages.success(request,'Product Updated Successfully', extra_tags='success')
            return redirect('home')
        else:
            Products_List.objects.filter(id=id).update(
                product_name = name,
                product_price = price, 
                product_status = False
            )
            messages.success(request,'Product Updated Successfully', extra_tags='success')
            return redirect('home')
    return render(request,'home.html')

def deleteproduct(req,id):
    print(id,'id')
    productsdelete = Products_List.objects.get(id=id)
    productsdelete.delete()
    messages.success(req,'Product Deleted Successfully', extra_tags='danger')
    return redirect('home')

@csrf_exempt
def delete_products(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('ids[]')
        products = Products_List.objects.filter(id__in=product_ids)
        products.delete()
        messages.success(request,'Products Deleted Successfully', extra_tags='danger')
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
