#!/bin/bash

echo "Me conecto al servidor windows por SSH y ejecuto el BAT"
#ssh -v zeneke@10.0.0.40 'c:\users\zeneke\mcscripts\runserver.bat'
ssh -i /home/zeneke/.ssh/id_rsa_windows zeneke@10.0.0.40 'c:\users\zeneke\mcscripts\runserver.bat'
