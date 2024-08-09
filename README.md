CS 361 assignment 8

Authenticator

The actor enters username and password in the UI. The point of the microservice is to check if the username and password is in the
database. The UI requests this status by having detect.py use the username and password and compare it to the dictionary in the database.
The status is the then determined by information from the check of the database. The detect.py file then writes the status to status.txt file.
The UI.py finally receives the status by reading the status.txt file. The UI then displays the status to the user.

![IMG_7800](https://github.com/user-attachments/assets/c2887477-0ab9-4dbc-bae0-56a1b206b488)
