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
* Documentation: http://number-recognizer.readthedocs.io/en/latest/


Requirements
------------

* OpenCV
* TensorFlow
* Numpy
* Pandas
* Click


Installation
------------

Install OpenCV_ and TensorFlow_ then and run::

	$ pip install number-recognizer

.. _OpenCV: https://github.com/milq/scripts-ubuntu-debian/blob/master/install-opencv.sh
.. _TensorFlow: https://www.tensorflow.org/versions/r0.10/get_started/os_setup.html#pip-installation


Usage
-----

Run::

	$ recognizer

Write a number on a clean peace of paper. Position it inside the green box in a way that the number is focused. Press **r** to recognize the number. Press **q** to quit the program.


Credits
---------
Tools used in rendering this package:

* Cookiecutter_
* `cookiecutter-pypackage`_


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pypackage`: https://github.com/condereis/cookiecutter-pypackage

