=================================
DLTN Ingestion 3 Config Generator
=================================

-----
About
-----

This generates a config.txt file to be shared with DPLA for DLTN ingests.  Rather than maintaining a single file, this
allows us to easily track the sets we are sharing with DPLA.  It also double checks for spelling errors etc. to ensure
we don't miss anything.

----------
How to Run
----------

This will generate a config.txt file you can share with DPLA:

.. code-block:: console

    $ python run.py

-----------------------------
Adding Providers and Datasets
-----------------------------

All datasets and providers are tracked in sets.yml.  You can add providers and datasets by editing this file.  It is
automatically read with run.py.

------------------------
Configuring Repox Lookup
------------------------

To ensure that you don't accidentally add a set that doesn't exist, this checks our Repox instance to ensure there are
no mispellings or related mistakes.  Make a copy of default_config.yml and copy it to config.yml.  Then, edit config.yml
replacing any default values with your Repox authentication information:

.. code-block:: console

    $ cp default_config.yml config.yml

