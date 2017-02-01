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


class ClassifierService(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClassifierService - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'prepare_settings': 'ClassifierPrepareSettings',
            'activate_settings': 'ClassifierActivateSettings',
            'id': 'str',
            'name': 'str',
            'alias': 'str',
            'description': 'str',
            'status': 'str',
            'type': 'str',
            'process_id_list': 'list[str]',
            'actual_process_id': 'str'
        }

        self.attribute_map = {
            'prepare_settings': 'PrepareSettings',
            'activate_settings': 'ActivateSettings',
            'id': 'Id',
            'name': 'Name',
            'alias': 'Alias',
            'description': 'Description',
            'status': 'Status',
            'type': 'Type',
            'process_id_list': 'ProcessIdList',
            'actual_process_id': 'ActualProcessId'
        }


        self._prepare_settings = None

        self._activate_settings = None

        self._id = None

        self._name = None

        self._alias = None

        self._description = None

        self._status = None

        self._type = None

        self._process_id_list = None

        self._actual_process_id = None



    @property
    def prepare_settings(self):
        """
        Gets the prepare_settings of this ClassifierService.


        :return: The prepare_settings of this ClassifierService.
        :rtype: ClassifierPrepareSettings
        """
        return self._prepare_settings

    @prepare_settings.setter
    def prepare_settings(self, prepare_settings):
        """
        Sets the prepare_settings of this ClassifierService.


        :param prepare_settings: The prepare_settings of this ClassifierService.
        :type: ClassifierPrepareSettings
        """
        self._prepare_settings = prepare_settings


    @property
    def activate_settings(self):
        """
        Gets the activate_settings of this ClassifierService.


        :return: The activate_settings of this ClassifierService.
        :rtype: ClassifierActivateSettings
        """
        return self._activate_settings

    @activate_settings.setter
    def activate_settings(self, activate_settings):
        """
        Sets the activate_settings of this ClassifierService.


        :param activate_settings: The activate_settings of this ClassifierService.
        :type: ClassifierActivateSettings
        """
        self._activate_settings = activate_settings


    @property
    def id(self):
        """
        Gets the id of this ClassifierService.
        Service unique identifier. It cannot be modified.

        :return: The id of this ClassifierService.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ClassifierService.
        Service unique identifier. It cannot be modified.

        :param id: The id of this ClassifierService.
        :type: str
        """
        self._id = id


    @property
    def name(self):
        """
        Gets the name of this ClassifierService.
        User-defined name for the service

        :return: The name of this ClassifierService.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ClassifierService.
        User-defined name for the service

        :param name: The name of this ClassifierService.
        :type: str
        """
        self._name = name


    @property
    def alias(self):
        """
        Gets the alias of this ClassifierService.
        Alias name of the service. Services can be accessed via this name.\r\nAlias can be modified. It is unique amongst the services.

        :return: The alias of this ClassifierService.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this ClassifierService.
        Alias name of the service. Services can be accessed via this name.\r\nAlias can be modified. It is unique amongst the services.

        :param alias: The alias of this ClassifierService.
        :type: str
        """
        self._alias = alias


    @property
    def description(self):
        """
        Gets the description of this ClassifierService.
        Service description

        :return: The description of this ClassifierService.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ClassifierService.
        Service description

        :param description: The description of this ClassifierService.
        :type: str
        """
        self._description = description


    @property
    def status(self):
        """
        Gets the status of this ClassifierService.
        New - the service was created | \r\nBusy - the service is working on something (e.g.: during the Prepare) | \r\nPrepared - the service was prepared so you can activate it to use | \r\nActive - the service so you can use it

        :return: The status of this ClassifierService.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ClassifierService.
        New - the service was created | \r\nBusy - the service is working on something (e.g.: during the Prepare) | \r\nPrepared - the service was prepared so you can activate it to use | \r\nActive - the service so you can use it

        :param status: The status of this ClassifierService.
        :type: str
        """
        allowed_values = ["New", "Busy", "Prepared", "Active"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status


    @property
    def type(self):
        """
        Gets the type of this ClassifierService.
        Type of the service.\r\nCurrently supported types:\r\n- Classifier\r\n- Prc

        :return: The type of this ClassifierService.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ClassifierService.
        Type of the service.\r\nCurrently supported types:\r\n- Classifier\r\n- Prc

        :param type: The type of this ClassifierService.
        :type: str
        """
        allowed_values = ["Classifier", "Prc", "Search"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type


    @property
    def process_id_list(self):
        """
        Gets the process_id_list of this ClassifierService.
        Contains all the process ids which belong to this service

        :return: The process_id_list of this ClassifierService.
        :rtype: list[str]
        """
        return self._process_id_list

    @process_id_list.setter
    def process_id_list(self, process_id_list):
        """
        Sets the process_id_list of this ClassifierService.
        Contains all the process ids which belong to this service

        :param process_id_list: The process_id_list of this ClassifierService.
        :type: list[str]
        """
        self._process_id_list = process_id_list


    @property
    def actual_process_id(self):
        """
        Gets the actual_process_id of this ClassifierService.


        :return: The actual_process_id of this ClassifierService.
        :rtype: str
        """
        return self._actual_process_id

    @actual_process_id.setter
    def actual_process_id(self, actual_process_id):
        """
        Sets the actual_process_id of this ClassifierService.


        :param actual_process_id: The actual_process_id of this ClassifierService.
        :type: str
        """
        self._actual_process_id = actual_process_id


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



