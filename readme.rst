AMQP asynchronous example
-------------------------

This repository contains a simple script to read from the amqp message bus from
`rabbit.opensuse.org <https://rabbit.opensuse.org>`_ using asyncio and `aio-pika
<https://aio-pika.readthedocs.io/en/latest/>`_.


Prerequisites
^^^^^^^^^^^^^

- Python 3.11+
- `poetry <https://python-poetry.org/>`_


Usage
^^^^^

.. code-block:: console

   ❯ poetry install
   ❯ poetry run ./amqp_listen.py
