{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ceab41cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import keras\n",
    "from PIL import Image, ImageOps\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "def machine_classification(img, weights_file):\n",
    "    # Load the model\n",
    "    model = keras.models.load_model(weights_file)\n",
    "\n",
    "    # Create the array of the right shape to feed into the keras model\n",
    "    data = np.ndarray(shape=(1, 100, 100, 3), dtype=np.float32)\n",
    "    image = img\n",
    "    #image sizing\n",
    "    size = (100, 100)\n",
    "    image = ImageOps.fit(image, size, Image.ANTIALIAS)\n",
    "\n",
    "    #turn the image into a numpy array\n",
    "    image_array = np.asarray(image)\n",
    "    # Normalize the image\n",
    "    normalized_image_array = (image_array.astype(np.float32) / 255)\n",
    "\n",
    "    # Load the image into the array\n",
    "    data[0] = normalized_image_array\n",
    "\n",
    "    # run the inference\n",
    "    prediction = model.predict(data)\n",
    "    return np.argmax(prediction) # return position of the highest probability"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
