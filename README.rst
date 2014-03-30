=======================
 SEA Directory Utility
=======================

The SEA Directory Utility is a command line tool that helps manage and
produce the SEA school's student directory.

To produce the directory, contact information is entered into a Google
Spreadsheet that follows a pre-defined format. The expected contents
are described in detail below in the section titled `Sheet Format`_.


Usage
=====

This section describes various usage examples. The name of the command
itself is `seadir`. Each of the different subcommands follows `seadir`
on the command line.


seadir clean
------------

The `seadir clean` command will process all the records in the
database and will perform any possible cleanups. These include:

  * Remove leading or trailing whitespace from all fields.
  * Standardize telephone number formats.
  * Add missing timestamp values.
  * Add missing Action field values.

This command modifies data on existing records, but only in
non-destructive ways.


seadir validate
---------------

The `seadir validate` command processes all the records and flags any
situations that seem erroneous. For example:

  * The same student listed in different classes.
  * Invalid email addresses.
  * Invalid phone numbers.

This command does not modify any data.


seadir generate
---------------

The `seadir generate` command produces the actual directory files.


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
  the field can have the value of `DELETE`, which means the prior
  records for this child should be removed from the finished
  directory.
