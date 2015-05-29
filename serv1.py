import requests
import json
from conf import *

class server1(object):
    @staticmethod
    def login():
        payload = '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"><soap:Header><context xmlns="urn:zimbra">'
        payload += '<userAgent name="ZimbraWebClient - SAF3 (Linux)"/>'
        payload += '<session/><format type="js"/></context></soap:Header><soap:Body><AuthRequest xmlns="urn:zimbraAdmin"><name>%s</name><password>%s</password>' %(login_server1, password_server1)
        payload += '<virtualHost>zimbra.labeip.epitech.eu</virtualHost></AuthRequest></soap:Body></soap:Envelope>'
        r = requests.post(zimbra_server1+"/service/admin/soap/AuthRequest", data=payload, verify=verify_ssl_server1)
        return r.status_code == 200, r.text

    @staticmethod
    def get_users(auth_token, offset=0, limit=900):
        payload = '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"><soap:Header><context xmlns="urn:zimbra"><userAgent name="ZimbraWebClient - SAF3 (Linux)"/><session id="332"/><format type="js"/><authToken>%s</authToken>' %auth_token
        payload += '</context></soap:Header><soap:Body><SearchDirectoryRequest xmlns="urn:zimbraAdmin" offset="%i" limit="%i" sortBy="name" sortAscending="1" applyCos="false" applyConfig="false" attrs="displayName,zimbraId,zimbraAliasTargetId,cn,sn,zimbraMailHost,uid,zimbraCOSId,zimbraAccountStatus,zimbraLastLogonTimestamp,description,zimbraIsDelegatedAdminAccount,zimbraIsAdminAccount,zimbraIsSystemResource,zimbraAuthTokenValidityValue,zimbraMailStatus,zimbraIsAdminGroup,zimbraCalResType,zimbraDomainType,zimbraDomainName,zimbraDomainStatus,zimbraIsDelegatedAdminAccount,zimbraIsAdminAccount,zimbraIsSystemResource" types="accounts">' %(offset, limit)
        payload += '<query></query></SearchDirectoryRequest></soap:Body></soap:Envelope>'
        r = requests.post(zimbra_server1+"/service/admin/soap/SearchDirectoryRequest", data=payload, verify=verify_ssl_server1)
        if r.status_code != 200:
            return False, json.loads(r.text)
        accounts = json.loads(r.text)['Body']['SearchDirectoryResponse']['account']
        total_accounts = json.loads(r.text)['Body']['SearchDirectoryResponse']['searchTotal']
        return True, accounts
                        
    @staticmethod
    def get_account_infos(auth_token, account_id):
        payload = '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"><soap:Header><context xmlns="urn:zimbra"><userAgent name="ZimbraWebClient - SAF3 (Linux)"/><session id="332"/><format type="js"/><authToken>%s</authToken>' %auth_token
        payload += '</context></soap:Header><soap:Body><BatchRequest xmlns="urn:zimbra" onerror="continue"><GetAccountRequest xmlns="urn:zimbraAdmin" applyCos="0"><account by="id">%s</account></GetAccountRequest>' %account_id
        payload += '<GetMailboxRequest xmlns="urn:zimbraAdmin"><mbox id="%s"></mbox></GetMailboxRequest>' %account_id
        payload += '<GetAccountMembershipRequest xmlns="urn:zimbraAdmin"><account by="id">%s</account></GetAccountMembershipRequest>' %account_id
        payload += '<GetAccountInfoRequest xmlns="urn:zimbraAdmin"><account by="id">%s</account></GetAccountInfoRequest>' %account_id
        payload += '<GetDataSourcesRequest xmlns="urn:zimbraAdmin"><id>%s</id></GetDataSourcesRequest></BatchRequest></soap:Body></soap:Envelope>' %account_id
        r = requests.post(zimbra_server1+"/service/admin/soap/BatchRequest", data=payload, verify=verify_ssl_server1)
        if r.status_code != 200:
            return False, json.loads(r.text)
        return True, json.loads(r.text)['Body']['BatchResponse']['GetAccountResponse']

    @staticmethod
    def get_mailing_lists(auth_token, limit=900, offset=0):
        payload = '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"><soap:Header><context xmlns="urn:zimbra"><userAgent name="ZimbraWebClient - SAF3 (Linux)"/><session id="321"/><format type="js"/><authToken>%s</authToken></context></soap:Header><soap:Body><SearchDirectoryRequest xmlns="urn:zimbraAdmin" offset="%i" limit="%i" sortBy="name" sortAscending="1" applyCos="false" applyConfig="false" attrs="displayName,zimbraId,zimbraMailHost,uid,description,zimbraIsAdminGroup,zimbraMailStatus,zimbraIsDelegatedAdminAccount,zimbraIsAdminAccount,zimbraIsSystemResource" types="distributionlists"><query></query></SearchDirectoryRequest></soap:Body></soap:Envelope>' %(auth_token, offset, limit)
        r = requests.post(zimbra_server1+"/service/admin/soap/SearchDirectoryRequest", data=payload, verify=verify_ssl_server1)
        if r.status_code != 200:
            return False, json.loads(r.text)
        return True, json.loads(r.text)['Body']['SearchDirectoryResponse']['dl']

    @staticmethod
    def get_mailing_list_distribution(auth_token, mailing_list_name, limit=900, offset=0):
        payload = '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"><soap:Header><context xmlns="urn:zimbra"><userAgent name="ZimbraWebClient - SAF3 (Linux)"/><session id="321"/><format type="js"/><authToken>%s</authToken></context></soap:Header><soap:Body><GetDistributionListRequest xmlns="urn:zimbraAdmin" limit="%i" offset="%i"><dl by="name">%s</dl><name>%s</name></GetDistributionListRequest></soap:Body></soap:Envelope>' %(auth_token, limit, offset, mailing_list_name, mailing_list_name)
        r = requests.post(zimbra_server1+"/service/admin/soap/GetDistributionListRequest", data=payload, verify=verify_ssl_server1)
        if r.status_code != 200:
            return False, json.loads(r.text)
        return True, json.loads(r.text)['Body']['GetDistributionListResponse']['dl']


    @staticmethod
    def get_aliases(auth_token, limit=900, offset=0):
        payload = '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"><soap:Header><context xmlns="urn:zimbra"><userAgent name="ZimbraWebClient - SAF3 (Linux)"/><session id="321"/><format type="js"/><authToken>%s</authToken></context></soap:Header><soap:Body><SearchDirectoryRequest xmlns="urn:zimbraAdmin" offset="%i" limit="%i" sortBy="name" sortAscending="1" applyCos="false" applyConfig="false" attrs="zimbraAliasTargetId,zimbraId,targetName,uid,type,description,zimbraIsDelegatedAdminAccount,zimbraIsAdminAccount,zimbraIsSystemResource" types="aliases"><query></query></SearchDirectoryRequest></soap:Body></soap:Envelope>' %(auth_token, offset, limit)
        r = requests.post(zimbra_server1+"/service/admin/soap/SearchDirectoryRequest", data=payload, verify=verify_ssl_server1)
        if r.status_code != 200:
            return False, json.loads(r.text)
        return True, json.loads(r.text)['Body']['SearchDirectoryResponse']['alias']
