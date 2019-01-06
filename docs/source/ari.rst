Automated Readability Index (ARI)
=================================

About
^^^^^

Unlike the other indices, the ARI, along with the Coleman-Liau, relies on a factor of characters per word, instead of the usual syllables per word. ARI is widely used on all types of texts. [reference]_

Usage
^^^^^

.. code-block:: python

    r = Readability(text)

    ari = r.ari()

    print(ari.score)
    print(ari.grade_levels)
    print(ari.ages)

References
----------

.. [reference] `readabilityformulas.com <http://www.readabilityformulas.com/automated-readability-index.php>`_