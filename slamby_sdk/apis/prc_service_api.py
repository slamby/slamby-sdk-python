# coding: utf-8

"""
PrcServiceApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient



class PrcServiceApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client


    def prc_activate_service(self, id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.prc_activate_service(id, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param str id:  (required)

        :param PrcActivateSettings prc_activate_settings: 

        :return: Process
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'prc_activate_settings']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prc_activate_service" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `prc_activate_service`")





        resource_path = '/api/Services/Prc/{id}/Activate'.replace('{format}', 'json')
        path_params = {}

        if 'id' in params:
            path_params['id'] = params['id']


        query_params = {}


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None

        if 'prc_activate_settings' in params:
            body_params = params['prc_activate_settings']


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Process',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response


    def prc_deactivate_service(self, id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.prc_deactivate_service(id, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param str id:  (required)

        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prc_deactivate_service" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `prc_deactivate_service`")



        resource_path = '/api/Services/Prc/{id}/Deactivate'.replace('{format}', 'json')
        path_params = {}

        if 'id' in params:
            path_params['id'] = params['id']


        query_params = {}


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response


    def prc_export_dictionaries(self, id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.prc_export_dictionaries(id, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param str id:  (required)

        :param ExportDictionariesSettings settings: 

        :return: Process
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'settings']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prc_export_dictionaries" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `prc_export_dictionaries`")





        resource_path = '/api/Services/Prc/{id}/ExportDictionaries'.replace('{format}', 'json')
        path_params = {}

        if 'id' in params:
            path_params['id'] = params['id']


        query_params = {}


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None

        if 'settings' in params:
            body_params = params['settings']


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Process',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response


    def prc_get_service(self, id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.prc_get_service(id, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param str id:  (required)

        :return: PrcService
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prc_get_service" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `prc_get_service`")



        resource_path = '/api/Services/Prc/{id}'.replace('{format}', 'json')
        path_params = {}

        if 'id' in params:
            path_params['id'] = params['id']


        query_params = {}


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PrcService',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response


    def prc_index_partial_service(self, id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.prc_index_partial_service(id, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param str id:  (required)

        :return: Process
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prc_index_partial_service" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `prc_index_partial_service`")



        resource_path = '/api/Services/Prc/{id}/IndexPartial'.replace('{format}', 'json')
        path_params = {}

        if 'id' in params:
            path_params['id'] = params['id']


        query_params = {}


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Process',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response


    def prc_index_service(self, id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.prc_index_service(id, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param str id:  (required)

        :param PrcIndexSettings prc_index_settings: 

        :return: Process
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'prc_index_settings']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prc_index_service" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `prc_index_service`")





        resource_path = '/api/Services/Prc/{id}/Index'.replace('{format}', 'json')
        path_params = {}

        if 'id' in params:
            path_params['id'] = params['id']


        query_params = {}


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None

        if 'prc_index_settings' in params:
            body_params = params['prc_index_settings']


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Process',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response


    def prc_keywords_service(self, id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.prc_keywords_service(id, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param str id:  (required)

        :param PrcKeywordsRequest request: 

        :param bool is_strict: 

        :return: list[PrcKeywordsResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'request', 'is_strict']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prc_keywords_service" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `prc_keywords_service`")







        resource_path = '/api/Services/Prc/{id}/Keywords'.replace('{format}', 'json')
        path_params = {}

        if 'id' in params:
            path_params['id'] = params['id']


        query_params = {}

        if 'is_strict' in params:
            query_params['isStrict'] = params['is_strict']


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None

        if 'request' in params:
            body_params = params['request']


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[PrcKeywordsResult]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response


    def prc_prepare_service(self, id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.prc_prepare_service(id, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param str id:  (required)

        :param PrcPrepareSettings prc_prepare_settings: 

        :return: Process
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'prc_prepare_settings']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prc_prepare_service" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `prc_prepare_service`")





        resource_path = '/api/Services/Prc/{id}/Prepare'.replace('{format}', 'json')
        path_params = {}

        if 'id' in params:
            path_params['id'] = params['id']


        query_params = {}


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None

        if 'prc_prepare_settings' in params:
            body_params = params['prc_prepare_settings']


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Process',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response


    def prc_recommend_by_id_service(self, id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.prc_recommend_by_id_service(id, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param str id:  (required)

        :param PrcRecommendationByIdRequest request: 

        :return: list[PrcRecommendationResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'request']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prc_recommend_by_id_service" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `prc_recommend_by_id_service`")





        resource_path = '/api/Services/Prc/{id}/RecommendById'.replace('{format}', 'json')
        path_params = {}

        if 'id' in params:
            path_params['id'] = params['id']


        query_params = {}


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None

        if 'request' in params:
            body_params = params['request']


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[PrcRecommendationResult]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response


    def prc_recommend_service(self, id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>

        >>> thread = api.prc_recommend_service(id, callback=callback_function)



        :param callback function: The callback function
            for asynchronous request. (optional)

        :param str id:  (required)

        :param PrcRecommendationRequest request: 

        :return: list[PrcRecommendationResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'request']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method prc_recommend_service" % key
                )
            params[key] = val
        del params['kwargs']



        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `prc_recommend_service`")





        resource_path = '/api/Services/Prc/{id}/Recommend'.replace('{format}', 'json')
        path_params = {}

        if 'id' in params:
            path_params['id'] = params['id']


        query_params = {}


        header_params = {}


        form_params = []
        local_var_files = {}


        body_params = None

        if 'request' in params:
            body_params = params['request']


        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[PrcRecommendationResult]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response


