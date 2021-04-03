from django.shortcuts import render

# Create your views here.
def register_sell(request):
    if request.method == "POST":
        print(request.data)
    print('GET')
    print(request)
    return render(
        request,
        template_name="sells/register_sales.html"
    )
