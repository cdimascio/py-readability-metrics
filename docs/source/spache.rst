SPACHE
===========


About
^^^^^

G. Spache devised the Spache Readability Formula in 1953 through an article, A New Readability Formula for Primary-Grade Reading Materials, published in The Elementary School Journal. The formula calculates the grade level of a text sample based on sentence length and number of unfamiliar words. The Spache Formula considers “unfamiliar words” as words that 3rd grade and below do not recognize. The Spache Formula is best used to calculate the difficulty of text that falls at the 3rd grade level or below. [reference]_

Usage
^^^^^

.. code-block:: python

    r = Readability(text)

    s = r.spache()

    print(s.score)
    print(s.grade_level)


References
----------

.. [reference] `readabilityformulas.com <https://www.readabilityformulas.com/spache-readability-formula.php>`_
    