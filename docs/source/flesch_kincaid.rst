Flesch-Kincaid Grade Level
==========================

About
^^^^^

Flesch readability scores are the most commonly cited and used of all readability scoring formula. 

The U.S. Army uses Flesch-Kincaid Grade Level for assessing the difficulty of technical manuals. The commonwealth of Pennsylvania uses Flesch-Kincaid Grade Level for scoring automobile insurance policies to ensure their texts are no higher than a ninth grade level of reading difficulty. Many other U.S. states also use Flesch-Kincaid Grade Level to score other legal documents such as business policies and financial forms. [reference]_

Usage
^^^^^

.. code-block:: python

    r = Readability(text)

    fk = r.flesch_kincaid()

    print(fk.score)
    print(fk.grade_level)

References
----------

.. [reference] `readabilityformulas.com <http://www.readabilityformulas.com/flesch-grade-level-readability-formula.php>`_