from django.shortcuts import render

def index(request):
    apps = [
      { 'title': 'System A', 'desc': '…', 'url': 'http://<IP-A>' },
      { 'title': 'System B', 'desc': '…', 'url': 'http://<IP-B>' },
      { 'title': 'Sensor Dashboard', 'desc': 'Interactive sand-station charts', 'url': '/sensors/' },
      { 'title': 'App D', 'desc': '…', 'url': 'http://<IP-D>' },
    ]
    return render(request, 'portal/index.html', { 'apps': apps })
