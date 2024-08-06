from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Meeting, Room
from .forms import MeetingForm

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})

def meetings_list(request):
    meetings = Meeting.objects.all()
    return render(request, "meetings/meetings.html", {"meetings": meetings})

@login_required
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.created_by = request.user
            meeting.save()
            messages.success(request, "Meeting successfully created!")
            return redirect('welcome')
        else:
            messages.error(request, "There was an error creating the meeting. Please check the form for errors.")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})

@login_required
def edit_meeting(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if meeting.created_by != request.user:
        messages.error(request, "You are not authorized to edit this meeting.")
        return redirect('welcome')
    
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            messages.success(request, "Meeting successfully updated!")
            return redirect('profile')
    else:
        form = MeetingForm(instance=meeting)
    return render(request, "meetings/edit.html", {"form": form})

@login_required
def delete_meeting(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if meeting.created_by != request.user:
        messages.error(request, "You are not authorized to delete this meeting.")
        return redirect('welcome')
    
    if request.method == "POST":
        meeting.delete()
        messages.success(request, "Meeting successfully deleted!")
        return redirect('profile')
    return render(request, "meetings/delete.html", {"meeting": meeting})
