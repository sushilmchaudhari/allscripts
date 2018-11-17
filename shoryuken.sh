#!/bin/bash 
# /etc/init.d/shoryuken start/stop 
#

APPDIR="/opt/msri/apps/staging/current"
PIDIR="/opt/msri/apps/staging/shared/tmp/pids"
LOGDIR="/opt/msri/apps/staging/shared/log"

function s_start () 
{ 
	echo  "Shoryuken: starting service" 
	`cd $APPDIR && bundle exec shoryuken --daemon --pidfile "$PIDIR/shoryuken.pid" --logfile "$LOGDIR/shoryuken.log" --config "$APPDIR/config/shoryuken.yml" --rails --require "$APPDIR/app/workers"`
 	sleep 5
	echo  "PID is $(cat $PIDIR/shoryuken.pid)"
}
 
function s_stop ( ) 
{ 
echo  "Shoryuken: stopping Service (PID = $(cat $PIDIR/shoryuken.pid) )" 
kill $(cat $PIDIR/shoryuken.pid) 
rm  $PIDIR/shoryuken.pid
 }
 
function s_status ( ) 
{ 
echo  "PID indicate indication file $(cat $PIDIR/shoryuken.pid)" 
ps  -ef  |  grep shoryuken |  grep -v grep | grep -v $0 
}
 
# Management instructions of the service 
case  "$1"  in 
	start)
		s_start
	;; 
	stop)
		s_stop
	;; 
	reload)
		s_stop
		sleep  1
		s_start
	;; 
	status)
		s_status
	;; 
	*) 
		echo  "Usage: $ 0 {start | stop | reload | status}" 
		exit  1 
	;; 
esac
 
exit  0
