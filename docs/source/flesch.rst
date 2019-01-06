Flesch-Kincaid Reading Ease
===========================

About
^^^^^

The U.S. Department of Defense uses the Reading Ease test as the standard test of readability for its documents and forms. Florida requires that life insurance policies have a Flesch Reading Ease score of 45 or greater.  [reference]_

Usage
^^^^^

.. code-block:: python

    r = Readability(text)

    f = r.flesch()

    print(f.score)
    print(f.ease)
    print(f.grade_levels)


References
----------

.. [reference] `readabilityformulas.com <http://www.readabilityformulas.com/flesch-reading-ease-readability-formula.php>`_