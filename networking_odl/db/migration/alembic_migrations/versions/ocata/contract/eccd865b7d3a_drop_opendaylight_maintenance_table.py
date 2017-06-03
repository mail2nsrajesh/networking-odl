# Copyright 2017 <PUT YOUR NAME/COMPANY HERE>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""drop opendaylight_maintenance table

Revision ID: eccd865b7d3a
Revises: fa0c536252a5
Create Date: 2017-05-24 03:00:40.194278

"""

# revision identifiers, used by Alembic.
revision = 'eccd865b7d3a'
down_revision = 'fa0c536252a5'

from alembic import op


def upgrade():
    op.drop_table('opendaylight_maintenance')