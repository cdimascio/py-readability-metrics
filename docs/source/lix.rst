Läsbarhetsindex
===============

About
^^^^^

Readability index for Swedish and other European Languages. [reference]_

Usage
^^^^^

.. code-block:: python

    r = Readability(text)

    f = r.lix()

    print(f.score)
    print(f.ease)


References
----------

.. [reference] `Lix (readability test) <https://en.wikipedia.org/wiki/Lix_(readability_test)>`_
