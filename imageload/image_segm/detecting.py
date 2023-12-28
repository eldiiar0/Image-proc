import pixellib
from pixellib.torchbackend.instance import instanceSegmentation

from django.shortcuts import render

def img_detect(request):
	if request.method == 'POST':
		a = request.POST['image_url']
		image_url= "C:/imgp/core"+a
		print(image_url)	
		segment_image = instanceSegmentation()
		segment_image.load_model("C:/imgp/core/imageload/pointrend_resnet50.pkl")
		target_class = segment_image.select_target_classes(person=True, car=True)
		result = segment_image.segmentImage(
			image_url,
			show_bboxes=True,
			segment_target_classes=target_class,
			# extract_segmented_objects=True,
			# save_extracted_objects=True,
			output_image_name="res2.jpg"
		)

	return render(request, 'imageload/main.html')