# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack.rds import rds_service
from openstack.rds.v3 import rdsresource as _rdsresource
from openstack import resource2 as resource


class Configurations(_rdsresource.Resource):
    base_path = '/configurations'
    resources_key = 'configurations'
    service = rds_service.RDSServiceV3()

    # capabilities
    allow_list = True

    id = resource.Body('id')
    spec_code = resource.Body('spec_code')
    name = resource.Body('name')
    description = resource.Body('description')
    datastore_version_name = resource.Body('datastore_version_name')
    datastore_name = resource.Body('datastore_name')
    created = resource.Body('created')
    updated = resource.Body('updated')
    user_defined = resource.Body('user_defined', type=bool)
