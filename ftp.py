#!/usr/bin/env python

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'


def main():
	try:
		f = ftplib.FTP(HOST)
	except (socket.error, socket.gaierror), e:
		print 'ERROR:cannot reach "%s"' % HOST
		return
     print '**** Connected to host "%s"' % HOST


     try:
     	f.login()
     except ftplib.error_perm:
     	print 'ERROR:cannot login anonymously'
     	f.quit()
     	return
     print '*** Logged in as "annonymously"'

     try:
     	f.cwd(DIRN)
     except ftplib.error_perm:
     	print 'ERROR: cannot CD to "%s"' % DIRN
     	f.quit()
     	return
     print '*** Changed to "%s"' % DIRN

     try:
     	f.retrbinary('RETR %s' % FILE, open(FILE, 'w').write)
     except ftplib.error_perm:
     	print 'ERROR: cannot read file "%s"' % FILE
     	os.unlink(FILE)
     else:
     	print '*** Download "%s" to CWD' % FILE
     f.quit()
     return

if __name__ == '__main__':
	main()
