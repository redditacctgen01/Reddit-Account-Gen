# Kill tor browser
# sudo kill -9 `ps -ef | grep "tor browser" | head -n1 | awk '{print $2}'`
sudo kill `pidof firefox.real`
# Kill tor
sudo kill `pidof tor`
sudo service tor restart
torbrowser-launcher
# TOR_PID=$(pgrep -o firefox.real); echo "$TOR_PID"
# sudo kill -15 "$TOR_PID" # Soft Kill of xed

# sudo kill -15 `sudo grep -o firefox`

# sudo service tor start
# tor