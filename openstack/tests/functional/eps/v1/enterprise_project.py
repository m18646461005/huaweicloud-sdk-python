import sys
import warnings
import os

from openstack import utils
from openstack import connection
utils.enable_logging(debug=True, stream=sys.stdout)
warnings.filterwarnings('ignore')
username = "xxxxxxx"
password = 'xxxxxxx'
userDomainId = "xxxxxxx"
auth_url = "https://iam.xxx.com:31943/v3"  # endpoint url
#os.environ.setdefault('OS_EPS_ENDPOINT_OVERRIDE', 'https://eps.br-iaas-odin1.huaweicloud.com/v1.0')

conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             domain_id=userDomainId,
                             username=username,
                             password=password,
                             verify=False)

def create_enterprise_project(_conn):
    data = {
    "name": "test56",
    "description": "test56"
    }
    res = _conn.eps.create_enterprise_project(**data)
    #for x in enterprise_projects:
    print res


def list_enterprise_projects(_conn):
    query = {
    "name": "test"
    }
    enterprise_projects = _conn.eps.list_enterprise_projects()
    #for x in enterprise_projects:
    print enterprise_projects


def get_enterprise_project(_conn):
    enterpriseProjectId = "0e00f529-7d13-4d47-8c62-496a27ecb3c6"
    result = _conn.eps.get_enterprise_project( enterpriseProjectId)
    print result

def enterprise_project_quotas(_conn):
    result = _conn.eps.enterprise_project_quotas()
    print  result

def update_enterprise_project(_conn):
    enterpriseProjectId = "0278f73a-c3dc-4089-99af-3cb2cf42f76b"
    data = {
        "name": "test008",
        "description": "test008"
    }
    result = _conn.eps.update_enterprise_project( enterpriseProjectId, **data)
    print result


def filter_resource_enterprise_project(_conn):
    enterpriseProjectId = "0278f73a-c3dc-4089-99af-3cb2cf42f76b"
    data = {
         "projects": ["0605767f6f00d5762ff9c001c70e7359"],
          "limit": 10,
          "offset": 0,
          "resource_types": ["ecs", "scaling_group", "images", "disk", "vpcs"]
    }
    result = _conn.eps.filter_resource_enterprise_project( enterpriseProjectId, **data)
    print result


def migrate_resource_enterprise_project(_conn):
    enterpriseProjectId = "0278f73a-c3dc-4089-99af-3cb2cf42f76b"
    data = {
        "project_id": "0605767f6f00d5762ff9c001c70e7359",
        "associated": False,
        "cloud_resource_type": "vpcs",
        "resource_id": "3dd93a56-2a1f-470e-91a4-3376ebde2fb6"
    }
    result = _conn.eps.migrate_resource_enterprise_project( enterpriseProjectId, **data)
    print result


if __name__ == '__main__':
    # create_enterprise_project(conn)
    # list_enterprise_projects(conn)
    get_enterprise_project(conn)
    # enterprise_project_quotas(conn)
    # update_enterprise_project(conn)
    # filter_resource_enterprise_project(conn)
    # migrate_resource_enterprise_project(conn)
    pass