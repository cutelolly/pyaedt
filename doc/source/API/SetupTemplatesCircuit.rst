Circuit  templates and arguments
================================

This section lists all setup templates with their default values and keys available in Circuit.

You can edit a setup after it is created. Here is an example:

.. code:: python

    from pyaedt import Hfss

    hfss = Hfss()
    # Any property of this setup can be found on this page.
    setup = hfss.create_setup()
    setup.props["AdaptMultipleFreqs"] = True
    setup.update()



.. pprint:: pyaedt.modules.SetupTemplates.NexximLNA
.. pprint:: pyaedt.modules.SetupTemplates.NexximDC
.. pprint:: pyaedt.modules.SetupTemplates.NexximTransient
.. pprint:: pyaedt.modules.SetupTemplates.NexximQuickEye
.. pprint:: pyaedt.modules.SetupTemplates.NexximVerifEye
.. pprint:: pyaedt.modules.SetupTemplates.NexximAMI

