# ram_check_flask
this code stores ram usage in the local db and returns the ram value at a specific time using flask API.

Command to access ram value: http://localhost:5000/ram/HH:MM:SS

This command will return the nearest time stamp and ram usage at that time.

This command will return the nearest timestamp and ram usage at that time.

## Acceptable input formats

The following input formats are acceptable:

* HH:MM:SS
* MM:SS
* SS
* HHMMSS
* MMSS
* SS

## Example

To get the ram usage at 12:00:00, use the following command:
http://localhost:5000/ram/12:00:00

This will return the nearest timestamp and ram usage at 12:00:00.
