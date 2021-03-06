# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VpnClientConfiguration(Model):
    """
    VpnClientConfiguration for P2S client

    :param vpn_client_address_pool: Gets or sets the reference of the Address
     space resource which represents Address space for P2S VpnClient.
    :type vpn_client_address_pool: :class:`AddressSpace
     <azure.mgmt.network.models.AddressSpace>`
    :param vpn_client_root_certificates: VpnClientRootCertificate for Virtual
     network gateway.
    :type vpn_client_root_certificates: list of
     :class:`VpnClientRootCertificate
     <azure.mgmt.network.models.VpnClientRootCertificate>`
    :param vpn_client_revoked_certificates: VpnClientRevokedCertificate for
     Virtual network gateway.
    :type vpn_client_revoked_certificates: list of
     :class:`VpnClientRevokedCertificate
     <azure.mgmt.network.models.VpnClientRevokedCertificate>`
    """ 

    _attribute_map = {
        'vpn_client_address_pool': {'key': 'vpnClientAddressPool', 'type': 'AddressSpace'},
        'vpn_client_root_certificates': {'key': 'vpnClientRootCertificates', 'type': '[VpnClientRootCertificate]'},
        'vpn_client_revoked_certificates': {'key': 'vpnClientRevokedCertificates', 'type': '[VpnClientRevokedCertificate]'},
    }

    def __init__(self, vpn_client_address_pool=None, vpn_client_root_certificates=None, vpn_client_revoked_certificates=None):
        self.vpn_client_address_pool = vpn_client_address_pool
        self.vpn_client_root_certificates = vpn_client_root_certificates
        self.vpn_client_revoked_certificates = vpn_client_revoked_certificates
