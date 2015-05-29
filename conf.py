#server 1

zimbra_server1 = "https://myoldzimbraserver.com:7071" #Your "old" server administration panel address (without the /admin)
login_server1 = "myadminlogin"
password_server1 = "myadminpassword"
verify_ssl_server1 = True

#server 2

server2_hostname = "mynewzimbraserver.com" #The destination server's fully qualified hostname on your network
server2_zimbra_ssh_key = "/home/lupin/.ssh/id_rsa.pub" #Path to a ssh key to connect to the destination server with the zimbra user
