Coleman Liau
============

The Coleman-Liau Formula usually gives a lower grade value than any of the Kincaid, ARI and Flesch values when applied to technical documents. [reference]_

.. code-block:: python

    r = Readability(text)

    cl = r.coleman_liau()

    print(cl.score)
    print(cl.grade_level)

References
----------

.. [reference] `readabilityformulas.com <http://www.readabilityformulas.com/coleman-liau-readability-formula.php>`_