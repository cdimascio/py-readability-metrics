Linsear Write
=============

About
^^^^^
Linsear Write is a readability metric for English text, purportedly developed for the United States Air Force to help them calculate the readability of their technical manuals. [reference]_

Usage
^^^^^

.. code-block:: python

    r = Readability(text)
    lw = r.linsear_write()

    print(lw.score)
    print(lw.grade_level)

References
----------

.. [reference] `readabilityformulas.com <http://www.readabilityformulas.com/linsear-write-readability-formula.php>`_