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


class SearchSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SearchSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'filter': 'Filter',
            'use_default_filter': 'bool',
            'weights': 'list[Weight]',
            'use_default_weights': 'bool',
            'response_field_list': 'list[str]',
            'search_field_list': 'list[str]',
            'type': 'str',
            'cut_off_frequency': 'float',
            'fuzziness': 'int',
            'count': 'int',
            'operator': 'str',
            'order': 'Order'
        }

        self.attribute_map = {
            'filter': 'Filter',
            'use_default_filter': 'UseDefaultFilter',
            'weights': 'Weights',
            'use_default_weights': 'UseDefaultWeights',
            'response_field_list': 'ResponseFieldList',
            'search_field_list': 'SearchFieldList',
            'type': 'Type',
            'cut_off_frequency': 'CutOffFrequency',
            'fuzziness': 'Fuzziness',
            'count': 'Count',
            'operator': 'Operator',
            'order': 'Order'
        }


        self._filter = None

        self._use_default_filter = None

        self._weights = None

        self._use_default_weights = None

        self._response_field_list = None

        self._search_field_list = None

        self._type = None

        self._cut_off_frequency = None

        self._fuzziness = None

        self._count = None

        self._operator = None

        self._order = None



    @property
    def filter(self):
        """
        Gets the filter of this SearchSettings.
        The Filter settings

        :return: The filter of this SearchSettings.
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this SearchSettings.
        The Filter settings

        :param filter: The filter of this SearchSettings.
        :type: Filter
        """
        self._filter = filter


    @property
    def use_default_filter(self):
        """
        Gets the use_default_filter of this SearchSettings.
        When you activate a Search service with a Filter, you can use this property to control if you want to use that 'default filter' during each searches

        :return: The use_default_filter of this SearchSettings.
        :rtype: bool
        """
        return self._use_default_filter

    @use_default_filter.setter
    def use_default_filter(self, use_default_filter):
        """
        Sets the use_default_filter of this SearchSettings.
        When you activate a Search service with a Filter, you can use this property to control if you want to use that 'default filter' during each searches

        :param use_default_filter: The use_default_filter of this SearchSettings.
        :type: bool
        """
        self._use_default_filter = use_default_filter


    @property
    def weights(self):
        """
        Gets the weights of this SearchSettings.
        Can use each available dataset field, a preferred value and a weighted score between 0 and 10 to boost the result

        :return: The weights of this SearchSettings.
        :rtype: list[Weight]
        """
        return self._weights

    @weights.setter
    def weights(self, weights):
        """
        Sets the weights of this SearchSettings.
        Can use each available dataset field, a preferred value and a weighted score between 0 and 10 to boost the result

        :param weights: The weights of this SearchSettings.
        :type: list[Weight]
        """
        self._weights = weights


    @property
    def use_default_weights(self):
        """
        Gets the use_default_weights of this SearchSettings.
        When you activate a Search service with Weights, you can use this property to control if you want to use that 'default weights' during each searches

        :return: The use_default_weights of this SearchSettings.
        :rtype: bool
        """
        return self._use_default_weights

    @use_default_weights.setter
    def use_default_weights(self, use_default_weights):
        """
        Sets the use_default_weights of this SearchSettings.
        When you activate a Search service with Weights, you can use this property to control if you want to use that 'default weights' during each searches

        :param use_default_weights: The use_default_weights of this SearchSettings.
        :type: bool
        """
        self._use_default_weights = use_default_weights


    @property
    def response_field_list(self):
        """
        Gets the response_field_list of this SearchSettings.
        Which dataset fields must be in the search response

        :return: The response_field_list of this SearchSettings.
        :rtype: list[str]
        """
        return self._response_field_list

    @response_field_list.setter
    def response_field_list(self, response_field_list):
        """
        Sets the response_field_list of this SearchSettings.
        Which dataset fields must be in the search response

        :param response_field_list: The response_field_list of this SearchSettings.
        :type: list[str]
        """
        self._response_field_list = response_field_list


    @property
    def search_field_list(self):
        """
        Gets the search_field_list of this SearchSettings.
        In which fields you would liket to search. The list can contains boosts. For example: title^2  which means matches on the title field will have twice the weight as those on the other fields

        :return: The search_field_list of this SearchSettings.
        :rtype: list[str]
        """
        return self._search_field_list

    @search_field_list.setter
    def search_field_list(self, search_field_list):
        """
        Sets the search_field_list of this SearchSettings.
        In which fields you would liket to search. The list can contains boosts. For example: title^2  which means matches on the title field will have twice the weight as those on the other fields

        :param search_field_list: The search_field_list of this SearchSettings.
        :type: list[str]
        """
        self._search_field_list = search_field_list


    @property
    def type(self):
        """
        Gets the type of this SearchSettings.
        The type of the search. Can be MATCH (default) which means a simple word based search or can be QUERY which means you can use expressions in the query, like in the [QueryString Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html#query-string-syntax) in ElasticSearch

        :return: The type of this SearchSettings.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SearchSettings.
        The type of the search. Can be MATCH (default) which means a simple word based search or can be QUERY which means you can use expressions in the query, like in the [QueryString Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html#query-string-syntax) in ElasticSearch

        :param type: The type of this SearchSettings.
        :type: str
        """
        allowed_values = ["Match", "Query"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type


    @property
    def cut_off_frequency(self):
        """
        Gets the cut_off_frequency of this SearchSettings.
        Allows specifying an absolute or relative document frequency where high frequency terms are moved into an optional subquery and are only scored if one of the low frequency (below the cutoff) terms in the case of an OR operator or all of the low frequency terms in the case of an AND operator match

        :return: The cut_off_frequency of this SearchSettings.
        :rtype: float
        """
        return self._cut_off_frequency

    @cut_off_frequency.setter
    def cut_off_frequency(self, cut_off_frequency):
        """
        Sets the cut_off_frequency of this SearchSettings.
        Allows specifying an absolute or relative document frequency where high frequency terms are moved into an optional subquery and are only scored if one of the low frequency (below the cutoff) terms in the case of an OR operator or all of the low frequency terms in the case of an AND operator match

        :param cut_off_frequency: The cut_off_frequency of this SearchSettings.
        :type: float
        """
        self._cut_off_frequency = cut_off_frequency


    @property
    def fuzziness(self):
        """
        Gets the fuzziness of this SearchSettings.
        Interpreted as a Levenshtein Edit Distance\u00E2\u20AC\u2030\u00E2\u20AC\u201D\u00E2\u20AC\u2030the number of one character changes that need to be made to one string to make it the same as another string. Can be specified as: -1 (generates an edit distance based on the length of the term) or 0, 1, 2 (the maximum allowed Levenshtein Edit Distance)

        :return: The fuzziness of this SearchSettings.
        :rtype: int
        """
        return self._fuzziness

    @fuzziness.setter
    def fuzziness(self, fuzziness):
        """
        Sets the fuzziness of this SearchSettings.
        Interpreted as a Levenshtein Edit Distance\u00E2\u20AC\u2030\u00E2\u20AC\u201D\u00E2\u20AC\u2030the number of one character changes that need to be made to one string to make it the same as another string. Can be specified as: -1 (generates an edit distance based on the length of the term) or 0, 1, 2 (the maximum allowed Levenshtein Edit Distance)

        :param fuzziness: The fuzziness of this SearchSettings.
        :type: int
        """
        self._fuzziness = fuzziness


    @property
    def count(self):
        """
        Gets the count of this SearchSettings.
        The maximum number of matches

        :return: The count of this SearchSettings.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this SearchSettings.
        The maximum number of matches

        :param count: The count of this SearchSettings.
        :type: int
        """
        self._count = count


    @property
    def operator(self):
        """
        Gets the operator of this SearchSettings.
        Can be set to OR or AND to control the operators between the text words\r\nFor example if the operator is AND, and the query is: 'white mobilephone' then the 'white' AND the 'mobilephone' must be match the documents\r\nIf the operator is OR in the same query then one of the query words is enough for a match. Of course if a document matches all the words then that will have a higher score

        :return: The operator of this SearchSettings.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this SearchSettings.
        Can be set to OR or AND to control the operators between the text words\r\nFor example if the operator is AND, and the query is: 'white mobilephone' then the 'white' AND the 'mobilephone' must be match the documents\r\nIf the operator is OR in the same query then one of the query words is enough for a match. Of course if a document matches all the words then that will have a higher score

        :param operator: The operator of this SearchSettings.
        :type: str
        """
        allowed_values = ["AND", "OR"]
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator`, must be one of {0}"
                .format(allowed_values)
            )
        self._operator = operator


    @property
    def order(self):
        """
        Gets the order of this SearchSettings.
        You can change the order of the search results. You have to specify a field of the dataset the order (Ascending or Descending)\r\nBe careful with this, if you change the default order then not the most relevant (for the text) documents will be on the top

        :return: The order of this SearchSettings.
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this SearchSettings.
        You can change the order of the search results. You have to specify a field of the dataset the order (Ascending or Descending)\r\nBe careful with this, if you change the default order then not the most relevant (for the text) documents will be on the top

        :param order: The order of this SearchSettings.
        :type: Order
        """
        self._order = order


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


