#!/usr/bin/python
import os,re,sys,pexpect
def read_ip_list(filename):
	ssh_newkey = 'Are you sure you want to continue connecting'
	iplistfile = sys.argv[1]
	count = 0
	for line in open(iplistfile):
		host = line.split(";")[0]
		passwd =line.split(";")[1]
		print host + "," + passwd
		cmd = pexpect.spawn('ssh-copy-id root@' + host)
		i = cmd.expect([ssh_newkey,'password:','authorized_keys','No route to host',pexpect.EOF,pexpect.TIMEOUT])
		if i==0:
			print "-----" + host.rstrip('\n') + "-----"
			print "say yes"
			cmd.sendline('yes')
			i = cmd.expect([ssh_newkey,'password:',pexpect.EOF])
		if i==1:
			print "-----" + host.rstrip('\n') + "-----"
			print "give passwd"
			cmd.sendline(passwd)
		if i==2:
			print "-----" + host.rstrip('\n') + "-----"
			print "either got key"
		if i==3:
			print "-----" + host.rstrip('\n') + "-----"
			print cmd.before
		if i==4:
			pass
		count += 1
	print("total ipcount:%d" % count)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Example: %s iplist.txt "%sys.argv[0])
        sys.exit()
    read_ip_list(sys.argv[1])
