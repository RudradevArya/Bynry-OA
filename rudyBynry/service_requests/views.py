from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'service_requests/request_list.html', {'requests': requests})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, user=request.user)
    return render(request, 'service_requests/request_detail.html', {'request': service_request})

def is_support_rep(user):
    return user.is_staff

@user_passes_test(is_support_rep)
def support_dashboard(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'service_requests/support_dashboard.html', {'requests': requests})

@user_passes_test(is_support_rep)
def update_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('support_dashboard')
    else:
        form = ServiceRequestForm(instance=service_request)
    return render(request, 'service_requests/update_request.html', {'form': form, 'request': service_request})