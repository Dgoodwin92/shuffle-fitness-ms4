from django.shortcuts import render, redirect

def view_bag(request):
    """ A view to return the bag contents page """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, membership_id):
    """ Add a membership to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if membership_id in list(bag.keys()):
        bag[membership_id] += quantity
    else:
        bag[membership_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
    