from django.shortcuts import render

#from django.core.files.storage import FileSystemStorage

#from django import forms
# Create your views here.
import platform

import os
from django.http import HttpResponse
from .forms import UploadForm
from .models import UploadedFile, UploadedLink
from django.utils import timezone

import datetime

def upload_file(request):
    if request.method == 'POST':

        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():

            os_name = platform.system()
            os_user = platform.uname
            browser = request.META.get('HTTP_USER_AGENT')
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


            with open('computer_info.txt', 'a') as f:
                f.write(f"{timestamp} - User: {os_user}, OS: {os_name}, Browser: {browser}\n")


            text_value = form.cleaned_data['text_field']
            file_value = form.cleaned_data['file_field']
            link_value = form.cleaned_data['link_field']

            selected_choice = form.cleaned_data['my_choice']

            # Створюємо шлях до каталогу
            today = timezone.now().date()
            base_path = os.path.join('media', str(today), selected_choice, text_value)
            os.makedirs(base_path, exist_ok=True)

            # Зберігаємо файл або посилання
            if file_value:
                file_instance = UploadedFile.objects.create(file=file_value)
                with open(os.path.join(base_path, file_value.name), 'wb+') as destination:
                    for chunk in file_value.chunks():
                        destination.write(chunk)

            if link_value:
                link_instance = UploadedLink.objects.create(link=link_value)
                with open(os.path.join(base_path, 'link.txt'), 'a') as f:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"[{timestamp}] {link_value}\n")                        

            return HttpResponse('Файл успішно завантажено або посилання збережено')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})