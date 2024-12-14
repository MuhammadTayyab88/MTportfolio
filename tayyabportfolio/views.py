from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Skills,CV,Profile
from django.http import FileResponse, Http404

# Render layout view
def layout_view(request):
    return render(request, 'layout.html')

# Download CV
def download_cv(request):
    try:
        cv = CV.objects.first()  # Get the first CV record
        if cv and cv.file:
            return FileResponse(open(cv.file.path, 'rb'), as_attachment=True, filename='Muhammad_tayyab.pdf')
        else:
            raise Http404("CV file not found")
    except FileNotFoundError:
        raise Http404("CV file not found")

# Profile View
def profile_view(request):
    profile = Profile.objects.first()  # Get the first profile record, change if you want multiple profiles
    return render(request, 'about.html', {'profile': profile})

# Contact Form Handling
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Ensure all fields are filled out
        if name and email and message:
            try:
                send_mail(
                    f"Message from {name}",
                    message,
                    email,
                    ['tayyibmuhammad1414@gmail.com'],  # Your email here
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully.")
                return redirect('contact_success')  # Redirect to the success page
            except Exception as e:
                messages.error(request, "There was an error sending your message. Please try again later.")
                return redirect('contact')
        else:
            messages.error(request, "Please fill in all fields.")
            return redirect('contact')

    return render(request, 'contact.html')

# Success Page after submitting contact form
def contact_success(request):
    return render(request, 'contact_success.html')

def skills_view(request):
    skills = Skills.objects.first()  # Fetch all skills
    print(skills)  # Debug: Print skills in the console
    return render(request, 'skil.html', {'skills': skills})
