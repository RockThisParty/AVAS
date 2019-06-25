wget -O vulners.nse
nmap -sV --script vulners.nse
nmap 127.0.0.1 -vv -sV -A > nmap_log.txt
grep "open port" nmap_log.txt > open_ports.txt