import cv2
import numpy as np 
from keras.models import load_model

################################################################

class Image:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(self.image_path)

    def scaledown_image(self, output_path):
        new_height = 28
        aspect_ratio = self.image.shape[1] / self.image.shape[0]
        new_width = int(new_height * aspect_ratio)
        zoomed_out_image = cv2.resize(self.image, (new_width, new_height))
        final_image = cv2.resize(zoomed_out_image, (28, 28))
        cv2.imwrite(output_path, final_image)

    def display_image(self):
        cv2.imshow('Original Image', self.image)
        scaled_image = cv2.imread('rescaled_img.png')
        cv2.imshow('Scaled Down Image', scaled_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def predict(self):
        model = load_model('models\handwritten_digit.model')
        img = cv2.imread('rescaled_img.png')[:,:,0]
        img = np.invert(np.array([img]))
        predictions = model.predict(img)
        print(f"Digit is {np.argmax(predictions)}" )


if __name__ == '__main__':
    try :
        img = str(input("Enter the path of image file :"))
        image_obj = Image(img)

        # Call the scaledown_image function
        image_obj.scaledown_image('rescaled_img.png')

        # Call the display_image function
        # image_obj.display_image()

        # Predict the image
        image_obj.predict()
    except Exception as e:
        if TypeError:
            print("WARNING : Remembere to save the image file into '.png' format.\n"*3)
        else :
            print(e,'\n')
        