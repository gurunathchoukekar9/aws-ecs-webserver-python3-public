#!/bin/bash

echo "Log: Inside Main.sh. Going to call ValidateEnv.sh"

sh ./ValidateEnv.sh

echo "Log: Inside Main.sh. Going to call Install_Python.sh"

sh ./Install_Python.sh

ls -l 

echo "Log: Inside Main.sh. Going for python3 Run_Flask_Server.py"
python3 Run_Flask_Server.py