from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Process
import subprocess
import os


active_processes = {}

# Create your views here.
def index(request):
    processes = Process.objects.all()
    context = {
        "processes" : processes
    }
    return render(request, "launcher/index.html", context)

def processhandler(request, pk):
    process = get_object_or_404(Process, name=str(pk))
    if process.name in active_processes.keys():
        active_processes[process.name].terminate()
        active_processes.pop(process.name)
        process.status = False
        process.save()
    else:
        active_processes[process.name] = subprocess.Popen(['python', f"{os.getcwd()}\{process.path}"])
        process.status = True
        process.save()
    return redirect(index)