from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .models import ClientProfile, ManagerProfile
# from .models import Notifications
from django.contrib.auth.models import User


def notifications_home(request):
    return render(request, 'notifications/home.html')


@login_required
def profile_view(request):
    if hasattr(request.user, 'client_profile'):
        profile = request.user.clientprofile
    elif hasattr(request.user, 'manager_profile'):
        profile = request.user.managerprofile
    else:
        profile = None
    return render(request, 'notifications/profile.html', {'profile': profile})


@login_required
def send_notifications(request):
    if request.method == 'POST':
        receiver_id = request.POST['receiver']
        message = request.POST['message']
        receiver = User.objects.get(id=receiver_id)
        Notifications.objects.create(sender=request.user, receiver=receiver, message=message)
        return redirect('view_notifications')
    users = User.objects.exclude(id=request.user.id)  # Exclude self from receiver list
    return render(request, 'notifications/send_notifications.html', {'users': users})

@login_required
def view_notifications(request):
    notifications = request.user.received_notifications.all()
    return render(request, 'notifications/view_notification.html', {'notifications': notifications})
