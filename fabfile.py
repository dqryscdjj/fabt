from fabric.api import env, hosts, roles, run

env.roledefs={
	'pbscore':['root@pbsbj:33287','root@pbssh:33287','root@pbssz:33287','root@pbsbjyz:33287',
		'root@pbswh:33287','root@pbscd:33287','root@pbslsj:33287'],
	'pbsgw':['root@pbsbjgw:33287','root@pbsshgw:33287','root@pbsszgw:33287'],
	'pbsall':['pbscore','pbsgw'],
	'ap' : ['hkvps','jpblog'],
	'us' : ['usdjj','uscd'],
	'bgscore': [
	#	'172.31.11.2',
		'172.31.12.2','172.31.21.2','172.31.22.2'
		],
	'bgsgateway': [
		'172.31.41.2','172.31.42.2','172.31.43.2',
		'172.31.51.2','172.31.52.2','172.31.53.2'],
	'bgsall':['bgscore','bgsgateway']
}
env.user = 'root'
env.password = 'root'
env.key_filename = '~/.ssh/root'
def hello():
	print("Hello world!")
	print("Executing on %s as %s" % (env.host, env.user))

def disstp():
	run("ovs-vsctl set bridge `ovs-vsctl show|grep Bridge|awk -F '\"' '{print $2}'` stp_enable=false")

def enbstp():
	run("ovs-vsctl set bridge `ovs-vsctl show|grep Bridge|awk -F '\"' '{print $2}'` stp_enable=true")

def setctrl():
	run("ovs-vsctl set-controller `ovs-vsctl show|grep Bridge|awk -F '\"' '{print $2}'` tcp:172.31.22.2:6633 tcp:172.31.12.2:6633 tcp:172.31.21.2:6633")

def delctrl():
	run("ovs-vsctl del-controller `ovs-vsctl show|grep Bridge|awk -F '\"' '{print $2}'`")
def delbr0():
	run("ovs-vsctl del-br br0")

def disflow():
	run("ovs-ofctl dump-flows `ovs-vsctl show|grep Bridge|awk -F '\"' '{print $2}'`")

def disdpflow():
	run("ovs-dpctl dump-flows `ovs-vsctl show|grep Bridge|awk -F '\"' '{print $2}'`")

def delflow():
	run("ovs-ofctl del-flows `ovs-vsctl show|grep Bridge|awk -F '\"' '{print $2}'`")

def shport():
	run("ovs-ofctl show `ovs-vsctl show|grep Bridge|awk -F '\"' '{print $2}'`")

def shss():
	run("ss -lntup ")

def shjava():
	run("ss -lntup | grep java");

def showiptables():
	run("iptables-save");
def addtcpportin():
	run("iptables -t filter -A INPUT -p tcp -m tcp -j ACCEPT");
def deltcpportin():
	run("iptables -t filter -D INPUT -p tcp -m tcp -j ACCEPT");
def killonos():
	run("ps aux  |  grep -i onos |  awk '{print $2}'|xargs sudo kill -9");
