from django.http import HttpResponse
from django.shortcuts import render
from ipware import get_client_ip
from ipware.utils import is_valid_ipv6


def index(request):
    address = get_client_ip(request)
    if is_valid_ipv6(address[0]):
        return render(request, "home.html", {"ip_address":address[0]})
    else:
        return render(request, "not_ipv6.html", {"ip_address": address[0]})