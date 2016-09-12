# coding: utf-8

"""
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""



from pprint import pformat
from six import iteritems


class PrcPrepareSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PrcPrepareSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data_set_name': 'str',
            'tag_id_list': 'list[str]',
            'compress_level': 'int',
            'compress_settings': 'CompressSettings'
        }

        self.attribute_map = {
            'data_set_name': 'DataSetName',
            'tag_id_list': 'TagIdList',
            'compress_level': 'CompressLevel',
            'compress_settings': 'CompressSettings'
        }


        self._data_set_name = None

        self._tag_id_list = None

        self._compress_level = None

        self._compress_settings = None



    @property
    def data_set_name(self):
        """
        Gets the data_set_name of this PrcPrepareSettings.


        :return: The data_set_name of this PrcPrepareSettings.
        :rtype: str
        """
        return self._data_set_name

    @data_set_name.setter
    def data_set_name(self, data_set_name):
        """
        Sets the data_set_name of this PrcPrepareSettings.


        :param data_set_name: The data_set_name of this PrcPrepareSettings.
        :type: str
        """
        self._data_set_name = data_set_name


    @property
    def tag_id_list(self):
        """
        Gets the tag_id_list of this PrcPrepareSettings.
        

        :return: The tag_id_list of this PrcPrepareSettings.
        :rtype: list[str]
        """
        return self._tag_id_list

    @tag_id_list.setter
    def tag_id_list(self, tag_id_list):
        """
        Sets the tag_id_list of this PrcPrepareSettings.
        

        :param tag_id_list: The tag_id_list of this PrcPrepareSettings.
        :type: list[str]
        """
        self._tag_id_list = tag_id_list


    @property
    def compress_level(self):
        """
        Gets the compress_level of this PrcPrepareSettings.
        

        :return: The compress_level of this PrcPrepareSettings.
        :rtype: int
        """
        return self._compress_level

    @compress_level.setter
    def compress_level(self, compress_level):
        """
        Sets the compress_level of this PrcPrepareSettings.
        

        :param compress_level: The compress_level of this PrcPrepareSettings.
        :type: int
        """
        self._compress_level = compress_level


    @property
    def compress_settings(self):
        """
        Gets the compress_settings of this PrcPrepareSettings.
        

        :return: The compress_settings of this PrcPrepareSettings.
        :rtype: CompressSettings
        """
        return self._compress_settings

    @compress_settings.setter
    def compress_settings(self, compress_settings):
        """
        Sets the compress_settings of this PrcPrepareSettings.
        

        :param compress_settings: The compress_settings of this PrcPrepareSettings.
        :type: CompressSettings
        """
        self._compress_settings = compress_settings


    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other



