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


class IThrottlingConfiguration(object):
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
        'default_throttle_policy': 'ThrottlePolicy',
        'assembly': 'object',
        'enabled': 'bool'
    }

    attribute_map = {
        'default_throttle_policy': 'defaultThrottlePolicy',
        'assembly': 'assembly',
        'enabled': 'enabled'
    }

    def __init__(self, default_throttle_policy=None, assembly=None, enabled=None):  # noqa: E501
        """IThrottlingConfiguration - a model defined in OpenAPI"""  # noqa: E501

        self._default_throttle_policy = None
        self._assembly = None
        self._enabled = None
        self.discriminator = None

        if default_throttle_policy is not None:
            self.default_throttle_policy = default_throttle_policy
        if assembly is not None:
            self.assembly = assembly
        if enabled is not None:
            self.enabled = enabled

    @property
    def default_throttle_policy(self):
        """Gets the default_throttle_policy of this IThrottlingConfiguration.  # noqa: E501


        :return: The default_throttle_policy of this IThrottlingConfiguration.  # noqa: E501
        :rtype: ThrottlePolicy
        """
        return self._default_throttle_policy

    @default_throttle_policy.setter
    def default_throttle_policy(self, default_throttle_policy):
        """Sets the default_throttle_policy of this IThrottlingConfiguration.


        :param default_throttle_policy: The default_throttle_policy of this IThrottlingConfiguration.  # noqa: E501
        :type: ThrottlePolicy
        """

        self._default_throttle_policy = default_throttle_policy

    @property
    def assembly(self):
        """Gets the assembly of this IThrottlingConfiguration.  # noqa: E501


        :return: The assembly of this IThrottlingConfiguration.  # noqa: E501
        :rtype: object
        """
        return self._assembly

    @assembly.setter
    def assembly(self, assembly):
        """Sets the assembly of this IThrottlingConfiguration.


        :param assembly: The assembly of this IThrottlingConfiguration.  # noqa: E501
        :type: object
        """

        self._assembly = assembly

    @property
    def enabled(self):
        """Gets the enabled of this IThrottlingConfiguration.  # noqa: E501


        :return: The enabled of this IThrottlingConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IThrottlingConfiguration.


        :param enabled: The enabled of this IThrottlingConfiguration.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, IThrottlingConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
