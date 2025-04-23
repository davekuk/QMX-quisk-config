# QMX-quisk-config
Configuration for QMX control on quisk

Add this file to quisk folder

Configure quisk and select QMX hardware file

Please note - you must have an instance of the rigctld running with command such as: 

    rigctld -m 2002 -r /dev/serial/by-id/usb-QRP_Labs_QMX_Transceiver-if00 -s 4800 -C stop_bits=2 &
