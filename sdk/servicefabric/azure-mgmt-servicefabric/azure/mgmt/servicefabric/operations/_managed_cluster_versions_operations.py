# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class ManagedClusterVersionsOperations(object):
    """ManagedClusterVersionsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The version of the Service Fabric resource provider API. This is a required parameter and it's value must be "2020-01-01-preview" for this specification. Constant value: "2020-01-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-01-01-preview"

        self.config = config

    def list_by_os(
            self, location, os_type, custom_headers=None, raw=False, **operation_config):
        """Gets the list of Service Fabric cluster code versions available for the
        specified OS type.

        Gets all available code versions for Service Fabric cluster resources
        by OS type.

        :param location: The location for the cluster code versions. This is
         different from cluster location.
        :type location: str
        :param os_type: The operating system of the cluster. Possible values
         include: 'Windows', 'Ubuntu', 'RedHat', 'Ubuntu18_04'
        :type os_type: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype:
         list[~azure.mgmt.servicefabric.models.ManagedClusterVersionDetails] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorModelException<azure.mgmt.servicefabric.models.ErrorModelException>`
        """
        # Construct URL
        url = self.list_by_os.metadata['url']
        path_format_arguments = {
            'location': self._serialize.url("location", location, 'str'),
            'osType': self._serialize.url("os_type", os_type, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorModelException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[ManagedClusterVersionDetails]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_by_os.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/managedclusters/locations/{location}/osType/{osType}/clusterVersions'}