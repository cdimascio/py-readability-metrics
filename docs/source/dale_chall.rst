Dale Chall Readability
======================

About
^^^^^

The Dale-Chall Formula is an accurate readability formula for the simple reason that it is based on the use of familiar words, rather than syllable or letter counts. Reading tests show that readers usually find it easier to read, process and recall a passage if they find the words familiar. [reference]_

Usage
^^^^^

.. code-block:: python

    r = Readability(text)

    dc = dale_chall()
    
    print(dc.score)
    print(dc.grade_levels)


References
----------

.. [reference] `readabilityformulas.com <http://www.readabilityformulas.com/new-dale-chall-readability-formula.php>`_