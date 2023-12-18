# from pixellib.instance import instance_segmentation
import pixellib
from pixellib.torchbackend.instance import instanceSegmentation


def object_detection_on_an_image():
    segment_image = instanceSegmentation()
    segment_image.load_model("./pointrend_resnet50.pkl")

    target_class = segment_image.select_target_classes(person=True, car=True)

    result = segment_image.segmentImage(
        "second.jpg",
        show_bboxes=True,
        segment_target_classes=target_class,
        # extract_segmented_objects=True,
        # save_extracted_objects=True,
        output_image_name="output2.jpg"
    )
    # print(result)
    print("_____")
    print(result["object_counts"])
    # print(result[0]["scores"])
    # objects_count = len(result[0]["scores"])
    # print(f"Total objects: {objects_count}")


def main():
    object_detection_on_an_image()


if __name__ == '__main__':
    main()