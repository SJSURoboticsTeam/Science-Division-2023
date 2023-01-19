#import the RamanAutomation class
from RAMAN_Automation import RamanAutomation


ip_address = '192.168.1.1' #ip address of remote machine
username = 'Robotics' #username for remote machine
password = 'Club' #password for remote machine
raman_exe = 'C:\\Users\\Robotics\\Desktop\\Raman\\Raman.exe' #path to Raman.exe on remote machine
excel_source = 'C:\\Users\\Robotics\\Desktop\\Raman\\Raman.xls' #path to excel file on remote machine
excel_dest = 'C:\\Users\\Robotics\\Desktop\\Raman\\Raman.xls' #path to desired location where file will be copied to

read_RAMAN = RamanAutomation(ip_address, username, password, raman_exe, excel_source, excel_dest)

ssh = read_RAMAN.ssh_connect()
read_RAMAN.run_exe()
read_RAMAN.copy_files()
read_RAMAN.close_ssh()