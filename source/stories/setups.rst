.. _stories:setups:

*******************************
Setting up the work environment
*******************************

All the AiiDA stories are designed and tested inside our virtual machines and with publicly available databases.
This allow users the possibility to set up the same work environment, and thus be able to obtain the same results when executing the described commands.

At the begining of each story you will have instructions on how to set things up.
Some of these are may be story-specific steps, but there are 3 steps that
Each story uses a particular version of AiiDA and/or works with a different database: 
but there is a common procedure to reproduce that environment.
You will need to:

Installing the virtual machine
..............................

At the begining of each story, there will 
You can find all virtual machines in the `Quantum Mobile website <https://www.materialscloud.org/work/quantum-mobile>`_.
Just click on the download button (which will take you to the the `github releases section <https://github.com/marvel-nccr/quantum-mobile/releases/>`_), search for the corresponding version, and follow the instructions.


Setting up a new profile
........................

Once you have your virtual machine up and running, it is also advisable that you set a different profile for each story.
This is because if you start mixing databases from different stories in the same profile, some of the commands may have different outputs and thus some procedures different behaviors.

You can do this by running the ``quicksetup`` command, and AiiDA will automatically create a new clean database to be used by it.
In the case below we chose to name the profile `storytest`, but you can use whatever name you prefer (just be consistent afterwards).
If you have not done so already, remember to first load the python environment by running ``workon aiida``.

.. code-block:: bash

    (aiida) max@qmobile:~$ verdi quicksetup 
        Info: enter "?" for help
        Info: enter "!" to ignore the default and set no value
        Profile name [quicksetup]: storytest
        User email [aiida@localhost]: 
        First name [Max]: 
        Last name [Scientist]: 
        Institution [Quantum Mobile]: 
        Warning: Found host 'localhost' but dropping '-h localhost' option for psql since this may cause psql to switch to password-based authentication.
        Success: created new profile `storytest`.
        Info: migrating the database.
        Operations to perform:
            Apply all migrations: auth, contenttypes, db
        Running migrations:
            Applying contenttypes.0001_initial... OK
            Applying contenttypes.0002_remove_content_type_name... OK
            Applying auth.0001_initial... OK
            Applying auth.0002_alter_permission_name_max_length... OK
            Applying auth.0003_alter_user_email_max_length... OK
            (...)
            Applying db.0042_prepare_schema_reset... OK
            Applying db.0043_default_link_label... OK
        Success: database migration completed.
    (aiida) max@qmobile:~$ 

Finally, you need to switch to this newly created profile by using ``verdi profile setdefault storytest`` before proceeding with any imports.

Importing an AiiDA database
...........................

Each story might use one or more AiiDA databases, indicated at the start of it.
These databases will tipically be found in the `Materials Cloud Archive <https://archive.materialscloud.org/>`_, but other sources are also possible.
In any case, the download link should be indicated together with the database.

You can either download the required databases and then move them into the virtual machine by using a `shared folder <https://www.virtualbox.org/manual/UserManual.html#sharedfolders>`_, or you can directly download them inside the virtual machine by using ``wget``.
For example, if you wanted to download the the `2D database <https://archive.materialscloud.org/record/2017.0008/v3>`_, you would need to run:

.. code-block:: bash

    wget 'https://archive.materialscloud.org/record/file?file_id=d1f3ac29-e3b0-400b-8109-8455be66160b&filename=two_dimensional_database.aiida&record_id=18' -O two_dimensional_database.aiida

Where the link used in the command is the one of the ``.aiida`` file that can be found in the `Files` section of the `archive entry <https://archive.materialscloud.org/record/2017.0008/v3>`_.
