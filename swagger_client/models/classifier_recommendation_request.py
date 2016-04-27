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


class ClassifierRecommendationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClassifierRecommendationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'text': 'str',
            'count': 'int',
            'use_emphasizing': 'bool',
            'need_tag_in_result': 'bool'
        }

        self.attribute_map = {
            'text': 'Text',
            'count': 'Count',
            'use_emphasizing': 'UseEmphasizing',
            'need_tag_in_result': 'NeedTagInResult'
        }


        self._text = None

        self._count = None

        self._use_emphasizing = None

        self._need_tag_in_result = None



    @property
    def text(self):
        """
        Gets the text of this ClassifierRecommendationRequest.


        :return: The text of this ClassifierRecommendationRequest.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this ClassifierRecommendationRequest.


        :param text: The text of this ClassifierRecommendationRequest.
        :type: str
        """
        self._text = text


    @property
    def count(self):
        """
        Gets the count of this ClassifierRecommendationRequest.


        :return: The count of this ClassifierRecommendationRequest.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this ClassifierRecommendationRequest.


        :param count: The count of this ClassifierRecommendationRequest.
        :type: int
        """
        self._count = count


    @property
    def use_emphasizing(self):
        """
        Gets the use_emphasizing of this ClassifierRecommendationRequest.


        :return: The use_emphasizing of this ClassifierRecommendationRequest.
        :rtype: bool
        """
        return self._use_emphasizing

    @use_emphasizing.setter
    def use_emphasizing(self, use_emphasizing):
        """
        Sets the use_emphasizing of this ClassifierRecommendationRequest.


        :param use_emphasizing: The use_emphasizing of this ClassifierRecommendationRequest.
        :type: bool
        """
        self._use_emphasizing = use_emphasizing


    @property
    def need_tag_in_result(self):
        """
        Gets the need_tag_in_result of this ClassifierRecommendationRequest.


        :return: The need_tag_in_result of this ClassifierRecommendationRequest.
        :rtype: bool
        """
        return self._need_tag_in_result

    @need_tag_in_result.setter
    def need_tag_in_result(self, need_tag_in_result):
        """
        Sets the need_tag_in_result of this ClassifierRecommendationRequest.


        :param need_tag_in_result: The need_tag_in_result of this ClassifierRecommendationRequest.
        :type: bool
        """
        self._need_tag_in_result = need_tag_in_result


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



