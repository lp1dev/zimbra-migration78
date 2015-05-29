from conf import *
from paramiko import SSHClient, AutoAddPolicy
from serv1 import server1

class server2(object):
    @staticmethod
    def add_redirection(targername, targetmail):
        script_path = "/opt/zimbra/bin/zmprov"
        cmd = '%s modifyAccount %s zimbraPrefMailForwardingAddress %s""' %(script_path, targetname, targetmail)
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(server2_hostname, username="zimbra", key_filename=server2_zimbra_ssh_key)
        stdin, stdout, stderr = client.exec_command(cmd)
        error = stderr.readlines()
        print(error)
        print(stdout.readlines())
        if len(error) == 0:
            return True, stdout.readlines()
        return False

    @staticmethod
    def create_alias(targetname, name):
        script_path = "/opt/zimbra/bin/zmprov"
        cmd = '%s aaa %s %s""' %(script_path, name, targetname)
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(server2_hostname, username="zimbra", key_filename="/home/lupin/.ssh/id_rsa.pub")
        stdin, stdout, stderr = client.exec_command(cmd)
        error = stderr.readlines()
        print(error)
        print(stdout.readlines())
        if len(error) == 0:
            return True, stdout.readlines()
        return False
    
    @staticmethod
    def set_properties(account):
        script_path = "/opt/zimbra/bin/zmprov"
        cmd = '%s modifyAccount %s ""' %(script_path, account)
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(server2_hostname, username="zimbra", key_filename="/home/lupin/.ssh/id_rsa.pub")
        stdin, stdout, stderr = client.exec_command(cmd)
        error = stderr.readlines()
        print(error)
        return len(error) == 0, stdout.readlines()

    @staticmethod
    def create_user(account):
        script_path = "/opt/zimbra/bin/zmprov"
        cmd = '%s ca %s ""' %(script_path, account)
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(server2_hostname, username="zimbra", key_filename="/home/lupin/.ssh/id_rsa.pub")
        stdin, stdout, stderr = client.exec_command(cmd)
        error = stderr.readlines()
        print(error)
        print(stdout.readlines())
        if len(error) == 0:
            return True, stdout.readlines()
        return False

    @staticmethod
    def get_ml_accounts(json_raw, token):
        accounts = ""
        success, value = server1.get_mailing_list_distribution(token, json_raw['name'])
        if len(value) > 0 and 'dlm' in value[0].keys():
            for account in value[0]['dlm']:
                accounts += " "+account['_content']
        return accounts
        
    @staticmethod        
    def add_users_to_ml(json_list, token):
        script_path = "/opt/zimbra/bin/zmprov"
        cmd = '%s adlm %s %s' %(script_path, json_list['name'], server2.get_ml_accounts(json_list, token))
        print(cmd)
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(server2_hostname, username="zimbra", key_filename="/home/lupin/.ssh/id_rsa.pub")
        stdin, stdout, stderr = client.exec_command(cmd)
        error = stderr.readlines()
        print(error)
        print(stdout.readlines())
        if len(error) == 0:
            return True, stdout.readlines()
        return False

    @staticmethod
    def create_ml(json_list, token):
        script_path = "/opt/zimbra/bin/zmprov"
        cmd = '%s cdl %s' %(script_path, json_list['name'])
        print(cmd)
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(server2_hostname, username="zimbra", key_filename="/home/lupin/.ssh/id_rsa.pub")
        stdin, stdout, stderr = client.exec_command(cmd)
        error = stderr.readlines()
        print(error)
        print(stdout.readlines())
        if len(error) == 0:
            return True, stdout.readlines()
        return False
