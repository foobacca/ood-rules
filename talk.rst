:title: OOD Rules
:data-transition-duration: 500
:css: talk.css

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
   :height: 500px
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

TODO: show code before refactor zoomed out

-----

.. code:: python

    def get_blank_activity(self):
        return {
            'nature': None,
            'type': None,
            'verbose_type': 'empty',
        }

    def add_period(self, period):
        # ...
        for halfday in xhalfdays(start_day, end_day):
            self.days[halfday] = {
                'nature': 'period',
                'type': period['type'],
                'verbose_type': self.period_legend.get(period['type']),
                'label': period.get('label'),
            }

    def add_symbol(self, symbol):
        # ...
        for halfday in xhalfdays_for_day(day):
            self.days[halfday] = {
                'nature': 'symbol',
                'type': symbol['type'],
                'verbose_type': self.symbol_legend.get(symbol['type']),
                'label': self.symbol_legend.get(symbol['type']),
            }

-----

TODO: show code after refactor zoomed out

-----


.. code:: python

    class Activity(object):

        def __init__(self, **kwargs):
            self.extra_init(**kwargs)

        def extra_init(self):
            # to be overridden by child classes
            pass

        def __unicode__(self):
            return "{} - {}/{} - {}".format(
                self.nature,
                self.activity_type,
                self.verbose_type,
                self.label
            )


    class EmptyActivity(Activity):
        def extra_init(self):
            self.nature = 'empty'
            self.activity_type = 0
            self.verbose_type = 'empty'
            self.label = 'empty'

        def __unicode__(self):
            return "empty"

-----

.. code:: python

    class PeriodActivity(Activity):
        def extra_init(self, activity_type, verbose_type, label=None):
            self.nature = 'period'
            self.activity_type = activity_type
            self.verbose_type = verbose_type
            if label:
                self.label = label
            else:
                self.label = verbose_type


    class SymbolActivity(Activity):
        def extra_init(self, activity_type, verbose_type):
            self.nature = 'symbol'
            self.activity_type = activity_type
            self.verbose_type = verbose_type
            self.label = verbose_type

        def __unicode__(self):
            return "{} - {}/{}".format(
                self.nature,
                self.activity_type,
                self.verbose_type,
            )

-----

.. code:: python

    def add_period(self, period):
        # ...
        for halfday in xhalfdays(start_day, end_day):
            self.days[halfday] = PeriodActivity(
                activity_type=period['type'],
                verbose_type=self.period_legend.get(period['type']),
                label=period.get('label')
            )

    def add_symbol(self, symbol):
        # ...
        for halfday in xhalfdays_for_day(day):
            self.days[halfday] = SymbolActivity(
                activity_type=symbol['type'],
                verbose_type=self.symbol_legend.get(symbol['type'])
            )

-----

Inheritance
-----------

Is it a good idea?
~~~~~~~~~~~~~~~~~~

------

Inheritance
-----------

Shallow and Narrow
~~~~~~~~~~~~~~~~~~

------


Django Class-Based Views
------------------------

UpdateView ancestry

.. image:: img/UpdateView-inheritance.svg
   :height: 600px

-----------

Open Closed
-----------

* **Open** for extension
* **Closed** for modification

-----------

super() vs extra_init()
-----------------------

.. code:: python

    class Activity(object):
        def __init__(self, **kwargs):
            # ...

    class PeriodActivity(Activity):
        def __init__(self, **kwargs):
            super(SymbolActivity, self).__init__(**kwargs)
            # ...

--------

super() vs extra_init()
-----------------------

.. image:: img/wrong-parent.jpg

-----------

super() vs extra_init()
-----------------------

.. code:: python

    class Activity(object):
        def __init__(self, **kwargs):
            # ...
            self.extra_init(**kwargs)

    class PeriodActivity(Activity):
        def extra_init(self, **kwargs):
            # ...

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
