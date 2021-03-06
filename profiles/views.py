from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from django.contrib import messages
from .forms import UserForm, ArtistForm, SelectorForm
from .models import UserProfile

from artworks.models import Artwork


def public_profile(request, user_id):
    """ A view to individual profiles"""
    profile = get_object_or_404(UserProfile, pk=user_id)
    artworks = Artwork.objects.all()

    template = 'profiles/public_profile.html'
    context = {
        'profile': profile,
        'artworks': artworks
    }
    return render(request, template, context)


@login_required
def profile(request):
    """ A view to individual profiles"""
    profile = get_object_or_404(UserProfile, user=request.user)
    artworks = Artwork.objects.all()
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'artworks': artworks,
        'orders': orders,
        'account_management': True
    }
    return render(request, template, context)


@login_required
def edit_profile(request, user_id):
    """ Edit profile details"""
    profile = get_object_or_404(UserProfile, user_id=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserForm(instance=profile)

    template = 'profiles/edit_profile.html'
    context = {
        'form': form,
        'profile': profile,
        'account_management': True
    }

    return render(request, template, context)


@login_required
def edit_artist(request, user_id):
    """ Edit artist profile details"""
    profile = get_object_or_404(UserProfile, user_id=request.user)

    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Public profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = ArtistForm(instance=profile)

    template = 'profiles/edit_artist.html'
    context = {
        'form': form,
        'profile': profile,
        'account_management': True
    }

    return render(request, template, context)


@login_required
def edit_selector(request, user_id):
    """ Edit if an account is artist or customer"""
    profile = get_object_or_404(UserProfile, user_id=request.user)

    if request.method == 'POST':
        form = SelectorForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile selector updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = SelectorForm(instance=profile)

    template = 'profiles/edit_selector.html'
    context = {
        'form': form,
        'profile': profile,
        'account_management': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_completed.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def delete_profile(request, user_id):
    """Delete Artworks"""
    superuser = request.user.is_superuser
    current_user = request.user.id
    original_artist = get_object_or_404(UserProfile, pk=user_id)

    if current_user != original_artist:
        if not superuser:
            messages.error(request, 'Only the Artist,' +
                           ' or Superuser can perform this action.')
    UserProfile.delete(self)
    messages.success(request, 'The account has been deleted!')
    return redirect(reverse('gallery'))
