import pixellib
from pixellib.torchbackend.instance import instanceSegmentation

from django.shortcuts import render
from .models import UploadedImage
from .forms import UploadImageForm

def main(request):
	
	if request.method == 'POST':
		form = UploadImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			pk=form.instance.id 
	else:
		form = UploadImageForm()
	try: 				
		upl_image = UploadedImage.objects.get(id=pk)
	except:
		upl_image = None

	return render(request, 'imageload/main.html', {'form': form, 'image': upl_image})


def homepage(request):
    return render(request, 'imageload/homepage.html')


def img_detect(request):
	if request.method == 'POST':
		image_url = request.POST['image_url']
		all_box = request.POST.get('all_obj')
		person_box = request.POST.get('person')
		car_box = request.POST.get('car')
		try: 				
			car_box = int(car_box)
		except:
			car_box = 0
		try: 				
			person_box = int(car_box)
		except:
			person_box = 0

		print(car_box, type(car_box))
		full_url= "C:/imgp/core"+image_url
		segment_image = instanceSegmentation()
		segment_image.load_model("C:/imgp/core/imageload/pointrend_resnet50.pkl")
		# target_class = segment_image.select_target_classes(person=1, car=1)
		result = segment_image.segmentImage(
			full_url,
			show_bboxes=True,
			# segment_target_classes=target_class,
			# extract_segmented_objects=True,
			# save_extracted_objects=True,
			output_image_name="C:/imgp/core/media/result.jpg"
		)

	return render(request, 'imageload/homepage.html')
