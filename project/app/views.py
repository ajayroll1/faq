


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import FAQ
# from django.contrib.auth.decorators import login_required

# # Custom Admin Dashboard View
# @login_required
# def custom_admin_dashboard(request):
#     faqs = FAQ.objects.all()  # Fetch all FAQs
#     return render(request, 'custom_admin/dashboard.html', {'faqs': faqs})

# # Add FAQ View
# @login_required
# def add_faq(request):
#     if request.method == "POST":
#         question = request.POST.get('question')
#         answer = request.POST.get('answer')
#         FAQ.objects.create(question=question, answer=answer)
#         return redirect('custom_admin')  # Redirect to admin dashboard
#     return render(request, 'custom_admin/add_faq.html')

# # Update FAQ View
# @login_required
# def update_faq(request, faq_id):
#     faq = get_object_or_404(FAQ, id=faq_id)
#     if request.method == "POST":
#         faq.question = request.POST.get('question')
#         faq.answer = request.POST.get('answer')
#         faq.save()
#         return redirect('custom_admin')  # Redirect to admin dashboard
#     return render(request, 'custom_admin/update_faq.html', {'faq': faq})

# # Delete FAQ View
# @login_required
# def delete_faq(request, faq_id):
#     faq = get_object_or_404(FAQ, id=faq_id)
#     faq.delete()
#     return redirect('custom_admin')  # Redirect to admin dashboard

# # Welcome Page View
# def welcome(request):
#     return render(request, 'welcome.html')       

# # FAQ Page View (Handles multiple languages)
# def faq_page(request):
#     lang = request.GET.get('lang', 'en')  # Default language 'en'
    
#     # Fetch all FAQs
#     faqs = FAQ.objects.all()
    
#     # Prepare the FAQ data, with translation for each question
#     data = []
#     for faq in faqs:
#         # Assuming `get_translated_question` is a method in your FAQ model
#         question = faq.get_translated_question(lang)
#         answer = faq.answer  # Answer remains the same (RichTextField)
        
#         data.append({
#             'id': faq.id,
#             'question': question,
#             'answer': answer
#         })
    
#     # Pass the data to the template
#     return render(request, 'app/faq_list.html', {'faqs': data})



from django.shortcuts import render, redirect, get_object_or_404
from .models import FAQ
from django.contrib.auth.decorators import login_required

# Custom Admin Dashboard View
@login_required
def custom_admin_dashboard(request):
    faqs = FAQ.objects.all()  # Fetch all FAQs
    return render(request, 'custom_admin/dashboard.html', {'faqs': faqs})

# Add FAQ View
@login_required
def add_faq(request):
    if request.method == "POST":
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        FAQ.objects.create(question=question, answer=answer)
        return redirect('custom_admin')  # Redirect to admin dashboard
    return render(request, 'custom_admin/add_faq.html')

# Update FAQ View
@login_required
def update_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    if request.method == "POST":
        question = request.POST.get('question')
        answer = request.POST.get('answer')

        if question and answer:
            faq.question = question
            faq.answer = answer
            faq.save()
            return redirect('custom_admin')  # Redirect to admin dashboard
    return render(request, 'custom_admin/update_faq.html', {'faq': faq})

# Delete FAQ View
@login_required
def delete_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    faq.delete()
    return redirect('custom_admin')  # Redirect to admin dashboard

# Welcome Page View
def welcome(request):
    return render(request, 'welcome.html')

# FAQ Page View (Handles multiple languages)
def faq_page(request):
    lang = request.GET.get('lang', 'en')  # Default language 'en'

    # Fetch all FAQs
    faqs = FAQ.objects.all()

    # Prepare the FAQ data with translation for each question
    data = [{
        'id': faq.id,
        'question': faq.get_translated_question(lang),  # Assuming translation method in model
        'answer': faq.answer  # Answer remains unchanged (RichTextField)
    } for faq in faqs]

    return render(request, 'app/faq_list.html', {'faqs': data})
