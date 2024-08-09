CS 361 Assignment 8

Authenticator

The actor enters the username and password in the UI. The point of the microservice is to check if the username and password are in the database. The UI requests this status by having detect.py use the username and password and compare it to the dictionary in the database. The status is then determined by information from the database check. The detect.py file then writes the status to the status.txt file. The UI.py finally receives the status by reading the status.txt file. The UI then displays the status to the user.


![IMG_7800](https://github.com/user-attachments/assets/f0af61f4-61b5-4aae-b4ac-06495fc30ca6)
