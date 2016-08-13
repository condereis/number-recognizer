===============================
Number Recognizer
===============================


.. image:: https://badge.fury.io/py/number-recognizer.svg
        :target: https://pypi.python.org/pypi/number-recognizer

.. image:: https://readthedocs.org/projects/number-recognizer/badge/?version=latest
        :target: https://number-recognizer.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


A software for the recognition of handwritten numbers. 

* Free software: BSD license
* Repository: https://github.com/condereis/number-recognizer


Requirements
------------

* OpenCV
* TensorFlow
* Numpy
* Pandas
* Click

Recognition Process
-------------------

* Get a grayscale version of the frame;
* Select a ROI;
* Apply a Gaussian Adaptive Threshold;
* Apply Median Blur to reduce noise;
* Apply Dilation also to reduce noise;
* Apply an AND operation on 3 consecutive frames to reduce noise;
* Find ROI Contours;
* Generate a square image that is white inside the contour and black outside, for each contour found.
* Resize image using linear interpolation to a 28x28 image, for each contour found;
* Run an Deep Convolutional Neural Network trained for MNIST dataset on each image. For more information on the model check `here <https://github.com/condereis/kaggle-mnist>`_.
* Concatenate de digits and print the number.


Credits
---------
Tools used in rendering this package:

* Cookiecutter_
* `cookiecutter-pypackage`_


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pypackage`: https://github.com/condereis/cookiecutter-pypackage

