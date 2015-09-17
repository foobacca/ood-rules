:title: OOD Rules
:data-transition-duration: 1500
:css: hovercraft.css

----

OOD Rules
=========

.. image:: img/planet-of-teh-ood.png

Hamish Downer / @hgd20 / github.com/foobacca

-----

The Rules
---------

-----

The Rules
---------

.. code:: python

    assert len(class) <= 100

-----

The Rules
---------

.. code:: python

    assert len(class) <= 100
    assert len(method) <= 5

-----

The Rules
---------

.. code:: python

    assert len(class) <= 100
    assert len(method) <= 5
    assert len(method.params) <= 4

-----

.. image:: img/free-the-ood.jpg

-----

The Rules
---------

.. code:: python

    assert len(class) <= 100
    assert len(method) <= 5
    assert len(method.params) <= 4

    class Meta:
        # you must persuade your pair
        # if you want to break a rule

-----

Example Time
------------

.. image:: img/tomsplanner-screenshot.png
   :height: 600px
   :width: 800px

-----

Example Time
------------

.. image:: img/tomsplanner-json-screenshot.png
   :height: 600px

-----

Example Time
------------

.. code:: json

    {
        "duration": 8,
        "durationtype": "day",
        "finishmoment": "09/22/2015 17:00:00 GMT",
        "id": "grid_0_33",
        "kids": [],
        "label": "Dalek",
        "nature": "period",
        "startmoment": "09/17/2015 09:00:00 GMT",
        "type": 26
    },

-----

Inheritance
-----------

Is it a good idea?

------

Inheritance
-----------

Django Class-Based Views

.. image:: img/UpdateView-inheritance.svg

-----------

Open Closed
-----------

* **Open** for extension
* **Closed** for modification

-----------

super() vs extra_init()
-----------------------

.. code:: python

    class PeriodActivity(Activity):
        def __init__(self, **kwargs):
            super(SymbolActivity, self).__init__(**kwargs)

--------

.. image:: img/wrong-parent.jpg

----------

.. image:: img/make-the-change-easy.png

-----

.. image:: img/pasta-ood.jpg

---------

Example 2
---------

---------

.. image:: img/ood-tea-cosy.jpg

---------

The Rules
---------

.. code:: python

    assert len(class) <= 100
    assert len(method) <= 5
    assert len(method.params) <= 4

    class Meta:
        # you must persuade your pair
        # if you want to break a rule

-----

Practical Object Oriented Design in Ruby
----------------------------------------

Sandi Metz

.. image:: img/poodr.jpeg

-----

.. image:: img/oods-in-your-favour.jpg

github.com/foobacca/ood-rules-talk
