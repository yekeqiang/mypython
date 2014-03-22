from ftp_module import FTPClient
import os

ftp_obj = FTPClient()

FTP_HOST = ""
FTP_USER = ""
FTP_PASS = ""
FTP_PORT = 21


# Connect to the server
ftp_obj.connect(FTP_HOST, FTP_USER, FTP_PASS, FTP_PORT)
print(ftp_obj.get_message())

directory = '/test'
ftp_obj.make_directory(directory)
print(ftp_obj.get_message())

app_root = os.path.dirname(os.path.abspath(__file__))
# Add the file name you want to upload
file_path = os.path.join(app_root, 'test.txt')
strip_path = file_path.rstrip(os.sep)
fp_path = os.path.basename(strip_path)


#Upload command
ftp_obj.upload_file(fp_path)
print(ftp_obj.get_message())

# Change Directory
ftp_obj.change_directory(directory)
print(ftp_obj.get_message())

# Add the filename to download
ftp_obj.download_file("hello.csv")
print(ftp_obj.get_message())
