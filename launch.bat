nmap.exe.lnk %1 -vv -sV -A > nmap_log.txt
findstr /C:"open port" nmap_log.txt > open_ports.txt