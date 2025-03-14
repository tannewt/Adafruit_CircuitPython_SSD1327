Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ssd1327/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/ssd1327/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_SSD1327.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_SSD1327
    :alt: Build Status

DisplayIO drivers for grayscale OLEDs driven by SSD1327


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

.. todo:: Remove the above note if PyPI version is/will be available at time of release.
   If the library is not planned for PyPI, remove the entire 'Installing from PyPI' section.

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-ssd1327/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-ssd1327

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-ssd1327

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-ssd1327

Usage Example
=============

.. code-block:: python

    import board
    import displayio
    import adafruit_ssd1327
    import busio
    import time

    displayio.release_displays()

    # This pinout works on a Metro and may need to be altered for other boards.
    spi = busio.SPI(board.SCL, board.SDA)
    tft_cs = board.D6
    tft_dc = board.D9
    tft_reset = board.D5

    display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset, baudrate=1000000)
    time.sleep(1)
    display = adafruit_ssd1327.SSD1327(display_bus, width=128, height=128)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_SSD1327/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
