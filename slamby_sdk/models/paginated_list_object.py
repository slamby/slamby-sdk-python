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


class PaginatedListObject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PaginatedListObject - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'items': 'list[object]',
            'count': 'int',
            'total': 'int',
            'scroll_id': 'str'
        }

        self.attribute_map = {
            'items': 'Items',
            'count': 'Count',
            'total': 'Total',
            'scroll_id': 'ScrollId'
        }


        self._items = None

        self._count = None

        self._total = None

        self._scroll_id = None



    @property
    def items(self):
        """
        Gets the items of this PaginatedListObject.
        Containing the actual displayed items. The type of the elements depend on the method

        :return: The items of this PaginatedListObject.
        :rtype: list[object]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this PaginatedListObject.
        Containing the actual displayed items. The type of the elements depend on the method

        :param items: The items of this PaginatedListObject.
        :type: list[object]
        """
        self._items = items


    @property
    def count(self):
        """
        Gets the count of this PaginatedListObject.
        The count of the actual returned items

        :return: The count of this PaginatedListObject.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this PaginatedListObject.
        The count of the actual returned items

        :param count: The count of this PaginatedListObject.
        :type: int
        """
        self._count = count


    @property
    def total(self):
        """
        Gets the total of this PaginatedListObject.
        The count of all items which are the pagination applied

        :return: The total of this PaginatedListObject.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this PaginatedListObject.
        The count of all items which are the pagination applied

        :param total: The total of this PaginatedListObject.
        :type: int
        """
        self._total = total


    @property
    def scroll_id(self):
        """
        Gets the scroll_id of this PaginatedListObject.
        Identifier for the next series of items where it is applicable

        :return: The scroll_id of this PaginatedListObject.
        :rtype: str
        """
        return self._scroll_id

    @scroll_id.setter
    def scroll_id(self, scroll_id):
        """
        Sets the scroll_id of this PaginatedListObject.
        Identifier for the next series of items where it is applicable

        :param scroll_id: The scroll_id of this PaginatedListObject.
        :type: str
        """
        self._scroll_id = scroll_id


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



