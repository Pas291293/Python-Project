from history_helper import history
import os

attribute = "accuracy"
history_dictionary = {
        attribute: [5, 6, 7, 8, 9]
    }
history_obj = history()
history_obj.set_history(history_dictionary)

current_dir = os.getcwd()
image_folder = os.path.join(os.path.join(current_dir, "test"), "test_data")
image_name = "test_image.png"
title = "Sample Image"
y_label = "Accuracy"
x_label = "epochs"
legend_location = "upper left"
colour = "r"

def get_image(history=history_obj, attribute=attribute,
          image_folder=image_folder, image_name=image_name,title=title, 
          y_label=y_label, x_label=x_label,legend_location=legend_location, colour=colour):
        image_path=os.path.join(image_folder, image_name)
        print(image_path)
        return image_path

get_image(history=history_obj, attribute=attribute,
          image_folder=image_folder, image_name=image_name,title=title, 
          y_label=y_label, x_label=x_label,legend_location=legend_location, colour=colour)     