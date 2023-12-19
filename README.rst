createadmin
==================

Create Django Admin Default Credentials
----------------------------------------

The `createadmin` package provides a Django management command, `createadmin`, that facilitates the creation of superuser default login credentials for the Django Admin Interface. This command is useful for setting up initial access to the admin interface during project development, packaging & deployment.

Installation
------------

To install the package, use the following pip command:

.. code-block:: bash

    pip install createadmin

After installation, add `'createadmin'` to the `INSTALLED_APPS` list in your project's `settings.py` file:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'createadmin',
        # ...
    ]

Usage
-----

### Default Credentials

To create a superuser with the default credentials (username: admin, password: admin, email: admin@example.com), run the following command in the terminal:

.. code-block:: bash

    python manage.py createadmin

### Custom Credentials

You can also create a superuser with custom credentials by adding a dictionary block to your project's `settings.py` file:

.. code-block:: python

    # settings.py

    CREATE_ADMIN = {
        'username': 'your_custom_username',
        'password': 'your_custom_password',
        'email': 'your_custom_email@example.com',
    }

Then, run the following command in the terminal:

.. code-block:: bash

    python manage.py createadmin

**Note:** Ensure that the `'createadmin'` app is included in your `INSTALLED_APPS` list before running the command.

Example
-------

Here's an example of using custom credentials in the `settings.py` file:

.. code-block:: python

    # settings.py

    INSTALLED_APPS = [
        # ...
        'createadmin',
        # ...
    ]

    CREATE_ADMIN = {
        'username': 'yash',
        'password': 'yash',
        'email': 'ychaudhari124@gmail.com',
    }

Run the following command in the terminal:

.. code-block:: bash

    python manage.py createadmin

This will create a superuser with the specified custom credentials.

**Note:** It is recommended to change the default or custom credentials once the initial setup is complete for security reasons.

---

*This package simplifies the process of creating Django Admin default credentials, making it more efficient for project setup, development, packaging & deployment.*