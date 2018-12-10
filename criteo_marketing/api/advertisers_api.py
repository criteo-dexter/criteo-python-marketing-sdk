# coding: utf-8

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    OpenAPI spec version: v.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from criteo_marketing.api_client import ApiClient


class AdvertisersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_campaigns(self, advertiser_id, authorization, **kwargs):  # noqa: E501
        """Gets all advertiser's campaigns  # noqa: E501

        Get the list of all the campaigns linked to the requested advertiser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_campaigns(advertiser_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int advertiser_id: Mandatory. The id of the advertiser to return. (required)
        :param str authorization: JWT Bearer Token (required)
        :return: list[CampaignMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_campaigns_with_http_info(advertiser_id, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_campaigns_with_http_info(advertiser_id, authorization, **kwargs)  # noqa: E501
            return data

    def get_campaigns_with_http_info(self, advertiser_id, authorization, **kwargs):  # noqa: E501
        """Gets all advertiser's campaigns  # noqa: E501

        Get the list of all the campaigns linked to the requested advertiser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_campaigns_with_http_info(advertiser_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int advertiser_id: Mandatory. The id of the advertiser to return. (required)
        :param str authorization: JWT Bearer Token (required)
        :return: list[CampaignMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['advertiser_id', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_campaigns" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'advertiser_id' is set
        if ('advertiser_id' not in local_var_params or
                local_var_params['advertiser_id'] is None):
            raise ValueError("Missing the required parameter `advertiser_id` when calling `get_campaigns`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in local_var_params or
                local_var_params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_campaigns`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'advertiser_id' in local_var_params:
            path_params['advertiserId'] = local_var_params['advertiser_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/advertisers/{advertiserId}/campaigns', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CampaignMessage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_categories(self, advertiser_id, authorization, **kwargs):  # noqa: E501
        """Gets all advertiser's categories  # noqa: E501

        Get the list of all the categories linked to the requested advertiser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_categories(advertiser_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int advertiser_id: Mandatory. The id of the advertiser to return. (required)
        :param str authorization: JWT Bearer Token (required)
        :param bool enabled_only: Optional. Returns only categories you can bid on. Defaults to false.
        :return: list[CampaignMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_categories_with_http_info(advertiser_id, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_categories_with_http_info(advertiser_id, authorization, **kwargs)  # noqa: E501
            return data

    def get_categories_with_http_info(self, advertiser_id, authorization, **kwargs):  # noqa: E501
        """Gets all advertiser's categories  # noqa: E501

        Get the list of all the categories linked to the requested advertiser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_categories_with_http_info(advertiser_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int advertiser_id: Mandatory. The id of the advertiser to return. (required)
        :param str authorization: JWT Bearer Token (required)
        :param bool enabled_only: Optional. Returns only categories you can bid on. Defaults to false.
        :return: list[CampaignMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['advertiser_id', 'authorization', 'enabled_only']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_categories" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'advertiser_id' is set
        if ('advertiser_id' not in local_var_params or
                local_var_params['advertiser_id'] is None):
            raise ValueError("Missing the required parameter `advertiser_id` when calling `get_categories`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in local_var_params or
                local_var_params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_categories`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'advertiser_id' in local_var_params:
            path_params['advertiserId'] = local_var_params['advertiser_id']  # noqa: E501

        query_params = []
        if 'enabled_only' in local_var_params:
            query_params.append(('enabledOnly', local_var_params['enabled_only']))  # noqa: E501

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/advertisers/{advertiserId}/categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CampaignMessage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_category(self, advertiser_id, category_hash_code, authorization, **kwargs):  # noqa: E501
        """Gets a specific advertiser's category  # noqa: E501

        Get a specific category linked to the requested advertiser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_category(advertiser_id, category_hash_code, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int advertiser_id: Mandatory. The id of the advertiser to return. (required)
        :param int category_hash_code: Mandatory. The id of the category to return. (required)
        :param str authorization: JWT Bearer Token (required)
        :return: list[CampaignMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_category_with_http_info(advertiser_id, category_hash_code, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_category_with_http_info(advertiser_id, category_hash_code, authorization, **kwargs)  # noqa: E501
            return data

    def get_category_with_http_info(self, advertiser_id, category_hash_code, authorization, **kwargs):  # noqa: E501
        """Gets a specific advertiser's category  # noqa: E501

        Get a specific category linked to the requested advertiser.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_category_with_http_info(advertiser_id, category_hash_code, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int advertiser_id: Mandatory. The id of the advertiser to return. (required)
        :param int category_hash_code: Mandatory. The id of the category to return. (required)
        :param str authorization: JWT Bearer Token (required)
        :return: list[CampaignMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['advertiser_id', 'category_hash_code', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_category" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'advertiser_id' is set
        if ('advertiser_id' not in local_var_params or
                local_var_params['advertiser_id'] is None):
            raise ValueError("Missing the required parameter `advertiser_id` when calling `get_category`")  # noqa: E501
        # verify the required parameter 'category_hash_code' is set
        if ('category_hash_code' not in local_var_params or
                local_var_params['category_hash_code'] is None):
            raise ValueError("Missing the required parameter `category_hash_code` when calling `get_category`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in local_var_params or
                local_var_params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_category`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'advertiser_id' in local_var_params:
            path_params['advertiserId'] = local_var_params['advertiser_id']  # noqa: E501
        if 'category_hash_code' in local_var_params:
            path_params['categoryHashCode'] = local_var_params['category_hash_code']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/advertisers/{advertiserId}/categories/{categoryHashCode}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CampaignMessage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
