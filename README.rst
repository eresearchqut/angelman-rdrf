Angelman
========

QUT eResearch Notes
-------------------

This repo has been created so we can build the docker image required to host the Global Angelman Registry using the legacy codebase from Murdoch University while we are transitioning the registry to the TRRF codebase.

It is a private repo fork of https://github.com/muccg/angelman.
Because it uses RDRF as a submodule we also created a private repo fork of https://github.com/muccg/rdrf at https://github.com/eresearchqut/muccg-rdrf.

The repository has the original MUCCG repository added as a remote in case you want to pull and merge in changes from them::

    ▶ git remote -v
    muccg-angelman	https://github.com/muccg/angelman.git (fetch)
    muccg-angelman	https://github.com/muccg/angelman.git (push)

Similarly, our RDRF clone also has the original repo set up as a remote::

    ▶ git remote -v
    muccg-rdrf	https://github.com/muccg/rdrf.git (fetch)
    muccg-rdrf	https://github.com/muccg/rdrf.git (push)

So far we applied security fixes that prevent patient downloading other patients Consent and CDE files and importing registries (https://github.com/eresearchqut/muccg-rdrf/pull/1).

The ```master`` and ``next_release`` branches of both the repositories have been resetted to version ``6.1.9``, which was the latest Angelman version released on the Murdoch University servers.

Then we applied the above mentioned security fixes and bumped to version up to ``7.0.0``, built the docker image and pushed it up to our ECR.

Making changes
^^^^^^^^^^^^^^

Most of the changes will happen in the RDRF repository.
Make your changes in ``next_release`` of https://github.com/eresearchqut/muccg-rdrf as required, create a Pull Request, code review, then merge it into ``master`` when it is ready, as you would usually do.

Decide the new version number of the RDRF (and Angelman as they share the version number) and set it in:

  * ``rdrf/rdrf/__init__.py``
  * ``rdrf/setup.py``

Example commit (https://github.com/eresearchqut/muccg-rdrf/commit/83d40e9e3735944778e1350c96fe12fd339c18ef)

Tag with the same version number::

    $ git tag -a Your.Version.Number -m 'Version Your.Version.Number'
    $ git push --tags

At this point the RDRF version is ready to be used.

In this repository, you will have to do at least the following changes to make a new release:

  * Update the ``rdrf`` submodule to the right version of ``rdrf``
  * Change the version number of ``muccg-rdrf`` in ``angelman/runtime-requirements.txt`` to be the version you picked above
  * Change ``angelman/angelman/__init__.py`` and ``angelman/setup.py`` to have the same version number

Commit your changes and again ``git tag -a`` with the new version number.

Your changes should be in ``master`` now and the ``tag`` should be pushed as well, as the scripts building the release will be ``git clone``-ing from the repository on GitHub ie. they don't work from your localy checked out source.

Run the following to create the docker image locally::

  $ ./develop.sh build base builder
  $ ./develop.sh run-builder
  $ ./develop.sh build prod

*Tips:* The ``run-builder`` command creates a ``angelman-Your.Version.Number-tar.gz`` in your ``build`` directory. You can un-tar it and inspect it to see what will end up in your docker image. The ``angelman`` source ends up in ``app`` the ``rdrf`` source in ``env/src/django-rdrf``.

The ``build prod`` command should build your image. Check that the version looks ok. Ex for version ``7.0.0``::

    Successfully built b01496362001
    Successfully tagged muccg/angelman:7.0.0

At this stage we have our docker image built locally.
We will have to upload this image to our ``ECR`` repository in the ``R1`` (Tools) account so we can pull it down to our ``EC2`` instance serving the app.

Here are the commands that worked at the time these notes were written. Please adjust as required (YOUR_VERSION should be the version you're deploying), ways of login, ECR account etc.)::

    # Assuming you are using saml2aws and your profile is named saml
    $ saml2aws login
    $ aws --profile saml ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 112652377709.dkr.ecr.ap-southeast-2.amazonaws.com/rdrf-angelman

    $ docker tag muccg/angelman:YOUR_VERSION 112652377709.dkr.ecr.ap-southeast-2.amazonaws.com/rdrf-angelman:YOUR_VERSION
    $ docker push 112652377709.dkr.ecr.ap-southeast-2.amazonaws.com/rdrf-angelman:YOUR_VERSION

Your new docker image is pushed and ready to be pulled down and used. Well done!

Talk to someone from Operations that you would like this image to be deployed.

Currently the ``docker-compose.yml`` file that references the docker image we use is in https://bitbucket.org/quteresearch/angelman-rdrf/.

About
-----

Angelman is a patient registry based on RDRF (https://muccg.github.io/rdrf/). During development, RDRF is installed as a git submodule::

    › git submodule status
    d28dfe3b313c1917dc4d46ac15adf5320d979cc3 rdrf (2.1.7)

Forgetting to update the git submodule is a common dev time error::

    › git submodule update
    Submodule path 'rdrf': checked out 'd28dfe3b313c1917dc4d46ac15adf5320d979cc3'

Refer to RDRF project for more docs.

Email:

rdrf@ccg.murdoch.edu.au

For developers
--------------

We do our development using Docker_ containers.
You will have to set up Docker on your development machine.

Other development dependencies are Python 2 and virtualenv_.

When cloning don't forget to install the rdrf submodule. To manually install sub modules after cloning, run:

    git submodule update --init --recursive

All the development tasks can be done by using the ``develop.sh`` shell script in this directory.
Please run it without any arguments for help on its usage.

A typical usage is::

    ./develop.sh build base
    ./develop.sh build builder
    ./develop.sh build dev
    ./develop.sh up

This will start up all the docker containers needed for dev.  You can then access the application on http://localhost:8000
You can login with one of the default users *admin/admin*.

.. _Docker: https://www.docker.com/
.. _docker-compose: https://docs.docker.com/compose/
.. _devdocs: https://rare-disease-registry-framework.readthedocs.io/en/latest/development.html

Contributing
------------

1. Fork ``next_release`` branch
2. Make changes on a feature branch
3. Submit pull request

