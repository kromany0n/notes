#!/bin/sh

# hanlding lock
LOCKFILE='/var/run/promtail_mysql_processlist.lock'

remove_lock() {
  rm -f "$LOCKFILE"
}

another_instance() {
  echo "There is another instance running with PID $(cat $LOCKFILE), exiting"
  exit 1
}

if [ -f "$LOCKFILE" ]; then
    if $(kill -0 "$(cat $LOCKFILE)") ; then
        pgrep processlist.sh | grep "$(cat $LOCKFILE)" >/dev/null && another_instance
    fi
fi

trap remove_lock EXIT
echo $$ > $LOCKFILE

# runnings script
sleep 20