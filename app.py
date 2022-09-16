{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2a6e444",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "st.title(\"Image Classification\")\n",
    "st.header(\"Retina Classification Project\")\n",
    "st.text(\"Upload a Retina Image for image classification\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2ac819e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from img_classification import machine_classification"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "baaaa424",
   "metadata": {},
   "outputs": [],
   "source": [
    "uploaded_file = st.file_uploader(\"Choose a Retina image ...\", type=\"jpg\")\n",
    "    if uploaded_file is not None:\n",
    "        image = Image.open(uploaded_file)\n",
    "        st.image(image, caption='Uploaded Image.', use_column_width=True)\n",
    "        st.write(\"\")\n",
    "        st.write(\"Classifying...\")\n",
    "        label = teachable_machine_classification(image, 'my_model.h5')\n",
    "        if label == 0:\n",
    "            st.write(\"The Eye has a problem\")\n",
    "        else:\n",
    "            st.write(\"The Eye is healthy\")"
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
