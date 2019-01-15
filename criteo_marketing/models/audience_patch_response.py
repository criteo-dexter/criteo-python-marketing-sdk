# coding: utf-8

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    OpenAPI spec version: v.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AudiencePatchResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'operation': 'str',
        'request_date': 'datetime',
        'schema': 'str',
        'nb_valid_identifiers': 'int',
        'nb_invalid_identifiers': 'int',
        'sample_invalid_identifiers': 'list[str]'
    }

    attribute_map = {
        'operation': 'operation',
        'request_date': 'requestDate',
        'schema': 'schema',
        'nb_valid_identifiers': 'nbValidIdentifiers',
        'nb_invalid_identifiers': 'nbInvalidIdentifiers',
        'sample_invalid_identifiers': 'sampleInvalidIdentifiers'
    }

    def __init__(self, operation=None, request_date=None, schema=None, nb_valid_identifiers=None, nb_invalid_identifiers=None, sample_invalid_identifiers=None):  # noqa: E501
        """AudiencePatchResponse - a model defined in OpenAPI"""  # noqa: E501

        self._operation = None
        self._request_date = None
        self._schema = None
        self._nb_valid_identifiers = None
        self._nb_invalid_identifiers = None
        self._sample_invalid_identifiers = None
        self.discriminator = None

        if operation is not None:
            self.operation = operation
        if request_date is not None:
            self.request_date = request_date
        if schema is not None:
            self.schema = schema
        if nb_valid_identifiers is not None:
            self.nb_valid_identifiers = nb_valid_identifiers
        if nb_invalid_identifiers is not None:
            self.nb_invalid_identifiers = nb_invalid_identifiers
        if sample_invalid_identifiers is not None:
            self.sample_invalid_identifiers = sample_invalid_identifiers

    @property
    def operation(self):
        """Gets the operation of this AudiencePatchResponse.  # noqa: E501

        The Operation recorded.  # noqa: E501

        :return: The operation of this AudiencePatchResponse.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this AudiencePatchResponse.

        The Operation recorded.  # noqa: E501

        :param operation: The operation of this AudiencePatchResponse.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def request_date(self):
        """Gets the request_date of this AudiencePatchResponse.  # noqa: E501

        When the Operation was recorded.  # noqa: E501

        :return: The request_date of this AudiencePatchResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._request_date

    @request_date.setter
    def request_date(self, request_date):
        """Sets the request_date of this AudiencePatchResponse.

        When the Operation was recorded.  # noqa: E501

        :param request_date: The request_date of this AudiencePatchResponse.  # noqa: E501
        :type: datetime
        """

        self._request_date = request_date

    @property
    def schema(self):
        """Gets the schema of this AudiencePatchResponse.  # noqa: E501

        The schema specified for the identifiers.  # noqa: E501

        :return: The schema of this AudiencePatchResponse.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this AudiencePatchResponse.

        The schema specified for the identifiers.  # noqa: E501

        :param schema: The schema of this AudiencePatchResponse.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def nb_valid_identifiers(self):
        """Gets the nb_valid_identifiers of this AudiencePatchResponse.  # noqa: E501


        :return: The nb_valid_identifiers of this AudiencePatchResponse.  # noqa: E501
        :rtype: int
        """
        return self._nb_valid_identifiers

    @nb_valid_identifiers.setter
    def nb_valid_identifiers(self, nb_valid_identifiers):
        """Sets the nb_valid_identifiers of this AudiencePatchResponse.


        :param nb_valid_identifiers: The nb_valid_identifiers of this AudiencePatchResponse.  # noqa: E501
        :type: int
        """

        self._nb_valid_identifiers = nb_valid_identifiers

    @property
    def nb_invalid_identifiers(self):
        """Gets the nb_invalid_identifiers of this AudiencePatchResponse.  # noqa: E501


        :return: The nb_invalid_identifiers of this AudiencePatchResponse.  # noqa: E501
        :rtype: int
        """
        return self._nb_invalid_identifiers

    @nb_invalid_identifiers.setter
    def nb_invalid_identifiers(self, nb_invalid_identifiers):
        """Sets the nb_invalid_identifiers of this AudiencePatchResponse.


        :param nb_invalid_identifiers: The nb_invalid_identifiers of this AudiencePatchResponse.  # noqa: E501
        :type: int
        """

        self._nb_invalid_identifiers = nb_invalid_identifiers

    @property
    def sample_invalid_identifiers(self):
        """Gets the sample_invalid_identifiers of this AudiencePatchResponse.  # noqa: E501

        Optionnal. A sample of invalid identifiers if there is some.  # noqa: E501

        :return: The sample_invalid_identifiers of this AudiencePatchResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._sample_invalid_identifiers

    @sample_invalid_identifiers.setter
    def sample_invalid_identifiers(self, sample_invalid_identifiers):
        """Sets the sample_invalid_identifiers of this AudiencePatchResponse.

        Optionnal. A sample of invalid identifiers if there is some.  # noqa: E501

        :param sample_invalid_identifiers: The sample_invalid_identifiers of this AudiencePatchResponse.  # noqa: E501
        :type: list[str]
        """

        self._sample_invalid_identifiers = sample_invalid_identifiers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AudiencePatchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
