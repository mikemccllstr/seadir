===============================
 SEA Student Directory Utility
===============================

The SEA Student Directory Utility is a command line tool that helps
manage and produce the SEA school's student directory.

To produce the directory, contact information is entered into a Google
Spreadsheet that follows a pre-defined format. The expected contents
are described in detail below in the section titled `Sheet Format`_.

Configuration
=============

Before you can use ``seadir`` for the first time, create a file in
your current directory named ``seadir.ini``. Populate it with content
like the following::

  [Response Data]
  email = youremail@example.com
  password = YOUR_SECRET_GOOGLE_PASSWORD
  spreadsheet = Student Directory Responses_Working
  worksheet = Form Responses

Note that absolutely everyone ought to be using Google's `2-Factor
authentication`_.  To make this tool work when you have it set up, you
need to create an `application-specific password`_.  The password you
set up on that page should be the one you enter in the config file.

.. _`2-Factor authentication`: https://support.google.com/accounts/answer/180744?hl=en
.. _`application-specific password`: https://accounts.google.com/b/0/IssuedAuthSubTokens?hl=en&hide_authsub=1


Usage
=====

This section describes various usage examples. The name of the command
itself is ``seadir``. Each of the different subcommands follows
``seadir`` on the command line.


Response Related Commands
-------------------------

These commands help manage the responses in the Google Sheet.


seadir res-dump
~~~~~~~~~~~~~~~

The ``seadir res-dump`` command prints out all the records from the
Google Sheet. It does not modify any data.


seadir res-clean
~~~~~~~~~~~~~~~~

The ``seadir res-clean`` command will process all the records in the
database and will perform any possible cleanups. These include:

  * Remove leading or trailing whitespace from all fields.
  * Standardize telephone number formats.
  * Add missing timestamp values.
  * Add missing Action field values.

This command modifies data on existing records, but only in
non-destructive ways.


seadir res-validate
~~~~~~~~~~~~~~~~~~~

The ``seadir res-validate`` command processes all the records and
flags any situations that seem erroneous. For example:

  * The same student listed in different classes.
  * Invalid email addresses.
  * Invalid phone numbers.

This command does not modify any data.


Directory Related Commands
--------------------------

These commands help produce the directory from the responses in the
Google Sheet.


seadir dir-generate
-------------------

The ``seadir dir-generate`` command produces the actual directory
files.


Sheet Format
============

The Google Spreadsheet document is the place where form submissions
are accumulated.

The Google Spreadsheet document is expected to have the following
fields:

Timestamp
  This is a date/time value when the record was entered. This value in
  this field should be automatically entered by Google when a form is
  submitted.

Student's Name
  This is the name of the student.

Classroom / Teacher
  This is the teacher in the classroom. There should be a defined list
  from which these values will come from. The format is "Grade #:
  Teacher Name". These values are used to group students into classes.

Submitter's email address
  This is the email address of the submitter. This field will be used
  to send the finished directory to the submitter, or to contact the
  submitter in case of questions. It will not be printed in the
  directory.

Contact's name
  Name of the first contact for the child.

Contact's phone number
  Telephone number of the first contact for the child, if it should be
  included in the directory.

Contact's alternate phone number
  Alternate telephone number of the first contact for the child, if it
  should be included in the directory.

Contact's email address
  Email address of the first contact for the child, if it should be
  included in the directory.

Contact's mailing address
  Mailing address of the first contact for the child, if it should be
  included in the directory.

Second Contact's name
  Name of the second contact for the child.

Second Contact's phone number
  Telephone number of the second contact for the child, if it
  should be included in the directory.

Second Contact's alternate phone number
  Alternate telephone number of the second contact for the child,
  if it should be included in the directory.

Second Contact's email address
  Email address of the second contact for the child, if it should
  be included in the directory.

Second Contact's mailing address
  Mailing address of the second contact for the child, if it
  should be included in the directory.

Action
  This field can be blank, indicating that the record is a normal
  entry, meaning the associated values should be printed in directory,
  replacing any that might have been submitted before. Alternatively,
  the field can have the value of ``DELETE``, which means the prior
  records for this child should be removed from the finished
  directory.
