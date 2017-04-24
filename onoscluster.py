from fabric.api import env, hosts, roles, run
from fabric.api import settings

env.roledefs={
	'tcore':['root@tbj:33287','root@tsh:33287','root@tsz:33287','root@tbjyz:33287',
		'root@twh:33287','root@tcd:33287','root@tlsj:33287'],
	'tysz':['root@tbjyz:33287','root@tsh:33287','root@tsz:33287'],
	'tyz':['root@tbjyz:33287'],
	'tsh':['root@tsh:33287'],
	'tsz':['root@tsz:33287']
}
env.user = 'root'
env.password = 'root'
env.key_filename = '~/.ssh/root'
def killonos():
	run("ps aux  |  grep -i onos|grep -v grep |  awk '{print $2}'|xargs sudo kill -9");
def resonos():
	run("rm -fr /opt/onos/apache-karaf-3.0.8/data/partitions/*");
	run("rm -fr /opt/onos/config/cluster.json");
	killonos();
	run("service onos start", pty=False);
def shonos():
	with settings(warn_only=True):
		run("ps -ef | grep onos");
	with settings(warn_only=True):
		run("ss -lntup | grep java");
def stonos():
	run("service onos start");
def recluster(jq = 'tcore'):
	if jq == 'tysz' :
		run("/opt/onos/bin/onos-form-cluster 10.242.1.100 10.248.1.246 10.252.1.250");
	else :
		run("/opt/onos/bin/onos-form-cluster 10.254.1.232 10.242.1.100 10.248.1.246 10.252.1.250 10.250.1.100 10.246.1.100 10.244.1.100");
	
