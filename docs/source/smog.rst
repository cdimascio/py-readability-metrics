SMOG
===========


About
^^^^^

The SMOG Readability Formula (Simple Measure of Gobbledygook) is a popular method to use on health literacy materials. [reference]_

Usage
^^^^^

.. code-block:: python

    r = Readability(text)

    s = r.smog()

    print(s.score)
    print(s.grade_level)


References
----------

.. [reference] `readabilityformulas.com <http://www.readabilityformulas.com/smog-readability-formula.php>`_
    