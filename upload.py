#!/usr/bin/env python  
import paramiko,datetime,os 
hostname='192.168.0.102'  
username='root'  
password='abc123'  
port=22  
local_dir='/tmp/'  
remote_dir='/tmp/test/' 
try: 
    t=paramiko.Transport((hostname,port))          
    t.connect(username=username,password=password)          
    sftp=paramiko.SFTPClient.from_transport(t)  
    #files=sftp.listdir(dir_path)          
    files=sftp.listdir(remote_dir)          
    for f in files:                  
        print ''                  
        print '#########################################'                  
        print 'Beginning to download file  from %s  %s ' % (hostname,datetime.datetime.now())                
        print 'Downloading file:',os.path.join(remote_dir,f) 
        sftp.get(os.path.join(remote_dir,f),os.path.join(local_dir,f))#下载               
        #sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f))#上传                 
        print 'Download file success %s ' % datetime.datetime.now()        
        print ''                  
        print '##########################################'   
    t.close() 
except Exception:  
       print "connect error!"  