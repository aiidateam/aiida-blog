.. _stories:

AiiDA user stories
------------------

This section contains a collection of stories inspired in real life use-cases of AiiDA.
You can use these stories to get a general feeling of what can be done with the code and what is like to work with it, as well as applyt the procedures in them as templates for when you need to perform similar tasks.

If you intend to reproduce the procedures ilustrated in these stories, it is **strongly recommended** that you set up a work environment that is as similar as possible to the one used to test them.
The easiest way to ensure this is to follow the next 3 steps:

1. Download the same `Quantum Mobile <https://www.materialscloud.org/work/quantum-mobile>`_ version that was used to design/test the story.
   If you already have that virtual machine, you can use the same.

2. Initialize a new profile to start with a clean database (see the ``quicksetup`` command in the `AiiDA documentation <https://aiida.readthedocs.io/projects/aiida-core/en/latest/intro/get_started.html#initialise-data-storage>`_).
   You will want to use a different profile for each story so that you don't get any `noise` from the other databases nodes.
   Remember to switch to this new profile by running ``verdi profile setdefault <PROFILE_NAME>``.

3. Download all the necessary AiiDA databases in your virtual machine and import them into your new profile.

It is **strongly recommended** that you first read the :ref:`Environment setup <stories:setups>` section, which will take you through the steps of setting up a clean work environment using a virtual machine.
This will allow you to have the same setup as the story, so that you can get the same results when using the same commands.
You can then start exploring variations from there, eventually being able to adapt the commands for your particular needs and for your specific database/version of the code.

.. toctree::
   :maxdepth: 1
   :hidden:
   
   0. Environment setups <./setups>

Here is the list of all available user stories:

.. toctree::
    :maxdepth: 1
    :numbered:

    ./browse_discover
