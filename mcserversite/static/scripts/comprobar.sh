((count = 2))                            # Maximum number to try.
while [[ $count -ne 0 ]] ; do
    ping -c 1 10.0.0.40 > /dev/null                      # Try once.
    rc=$?
    if [[ $rc -eq 0 ]] ; then
        ((count = 1))                      # If okay, flag to exit loop.
    fi
    ((count = count - 1))                  # So we don't go forever.
done

if [[ $rc -eq 0 ]] ; then                  # Make final determination.
    echo "Esta encendido"
    echo "encendido" > /home/zeneke/www/mcserver/mcserversite/static/status/server.txt
else
    echo "APAGADO, ejecutar encendido"
    echo "apagado" > /home/zeneke/www/mcserver/mcserversite/static/status/server.txt
fi
