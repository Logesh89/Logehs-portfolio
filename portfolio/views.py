from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact
from django.core.mail import send_mail

# ✅ Render the landing page correctly
def default(request):
    return render(request, 'default.html')

# ✅ Render the home page
def home(request):
    return render(request, 'home.html')

# ✅ Render the myresume page
def myresume(request):
    return render(request, 'myresume.html')

# ✅ Render the about page
def about(request):
    return render(request, 'about.html')

# ✅ Blog handling function (ensure Blogs model exists)
def handleblog(request):
    posts = Blogs.objects.all()  # type: ignore
    context = {"posts": posts}
    return render(request, 'handleblog.html', context)

# ✅ Contact function (Handles form submission & email sending)
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("num")
        message = request.POST.get("desc")

        # ✅ Save contact details in the database
        query = Contact(name=name, email=email, phonenumber=phone, description=message)
        query.save()

        # ✅ Prepare email subject and body
        subject = f"📩 New Connect from Your Portfolio-site from {name} - {email}"
        email_body = f"""
        Heyy!! LOGESH,

        You have received a new contact from Portfolio-site:

        👤 Name: {name}
        ✉️ Email: {email}
        📞 Phone: {phone}
        📝 Message: {message}

        Best Regards,
        LOGESH S
        """

        # ✅ Send email notification
        try:
            send_mail(
                subject,  # Updated subject
                email_body,
                "logeshsubramani89@gmail.com",  # Sender email
                ["logeshsubramani89@gmail.com"],  # Your email to receive notifications
                fail_silently=False,
            )
            messages.success(request, "Thanks for contacting us. We will get back to you soon!")
            print("✅ Email sent successfully!")

        except Exception as e:
            print(f"❌ Email Error: {e}")
            messages.error(request, "Failed to send email. Please try again later.")

        # ✅ Redirect to prevent form resubmission
        return redirect('/contact/')

    return render(request, 'contact.html')  
