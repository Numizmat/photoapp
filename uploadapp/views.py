from django.shortcuts import render
from .forms import ImageForm, SaveImgForm, SaveForm, SaveImg


def upload(request):
    return render(request, 'uploadapp/upload.html')


def create_to_img(request):
    user = request.user
    if request.method == 'POST':
        form = SaveForm(request.POST)
        file_form = SaveImgForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid() and file_form.is_valid():
            feed_instance = form.save(commit=False)
            feed_instance.user = user
            feed_instance.save()
            for f in files:
                file_instance = SaveImg(file=f, feed=feed_instance)
                img_obj = file_instance.save
                return render(request, 'uploadapp/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = SaveForm()
        file_form = SaveImgForm()
        return render(request, 'uploadapp/upload.html', {'form': form})


class SaveImgView(SaveImgForm):
    form_class = SaveImgForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'uploadapp/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'uploadapp/upload.html', {'form': form})



# def upload(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'mainapp/../templates/uploadapp/upload.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'mainapp/../templates/uploadapp/upload.html', {'form': form})
#
