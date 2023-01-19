import paramiko
import time

class RamanAutomation:
    def __init__(self, ip, username, password, raman_exe, excel_source, excel_dest):
        self.ip = ip
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, username=self.username, password=self.password)
        self.raman_exe = raman_exe
        self.excel_source = excel_source
        self.excel_dest = excel_dest

    def run_exe(self):
        stdin, stdout, stderr = self.ssh.exec_command(self.raman_exe)
        time.sleep(10)
        return stdin, stdout, stderr

    def copy_files(self):
        sftp = self.ssh.open_sftp()
        sftp.put(self.excel_source, self.excel_dest)
        sftp.close()

    def close_ssh(self):
        self.ssh.close()