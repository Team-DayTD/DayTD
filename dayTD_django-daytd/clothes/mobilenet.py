import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import Model
from PIL import Image

class FeatureExtractor:
    def __init__(self):
        # Use mobilenet as the architecture and ImageNet for the weight
        base_model = tf.keras.applications.mobilenet.MobileNet(weights='imagenet')
        # Customize the model to return features from fully-connected layer
        self.model = Model(inputs=base_model.input, outputs=base_model.get_layer('reshape_2').output)

    def extract(self, img):
        # Resize the image
        img = np.resize(img, (224, 224))
        # Convert the image color space
        img = Image.fromarray(img)
        img = img.convert('RGB')
        # Reformat the image
        x = tf.keras.utils.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        # Extract Features
        feature = self.model.predict(x)[0]
        return feature / np.linalg.norm(feature)