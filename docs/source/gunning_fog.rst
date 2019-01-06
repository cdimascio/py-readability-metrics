Gunning Fog
===========


About
^^^^^

The Gunning fog index measures the readability of English writing. The index estimates the years of formal education needed to understand the text on a first reading. A fog index of 12 requires the reading level of a U.S. high school senior (around 18 years old). [reference]_

Usage
^^^^^

.. code-block:: python

    r = Readability(text)

    gf = r.gunning_fog()

    print(gf.score)
    print(gf.grade_level)

References
----------

.. [reference] `readabilityformulas.com <http://www.readabilityformulas.com/gunning-fog-readability-formula.php>`_