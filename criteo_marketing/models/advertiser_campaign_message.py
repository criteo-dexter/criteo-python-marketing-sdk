# coding: utf-8

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    The version of the OpenAPI document: v.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AdvertiserCampaignMessage(object):
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
        'id': 'int',
        'campaign_name': 'str',
        'campaign_status': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'campaign_name': 'campaignName',
        'campaign_status': 'campaignStatus',
        'status': 'status'
    }

    def __init__(self, id=None, campaign_name=None, campaign_status=None, status=None):  # noqa: E501
        """AdvertiserCampaignMessage - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._campaign_name = None
        self._campaign_status = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if campaign_name is not None:
            self.campaign_name = campaign_name
        if campaign_status is not None:
            self.campaign_status = campaign_status
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this AdvertiserCampaignMessage.  # noqa: E501


        :return: The id of this AdvertiserCampaignMessage.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdvertiserCampaignMessage.


        :param id: The id of this AdvertiserCampaignMessage.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def campaign_name(self):
        """Gets the campaign_name of this AdvertiserCampaignMessage.  # noqa: E501


        :return: The campaign_name of this AdvertiserCampaignMessage.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this AdvertiserCampaignMessage.


        :param campaign_name: The campaign_name of this AdvertiserCampaignMessage.  # noqa: E501
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def campaign_status(self):
        """Gets the campaign_status of this AdvertiserCampaignMessage.  # noqa: E501


        :return: The campaign_status of this AdvertiserCampaignMessage.  # noqa: E501
        :rtype: str
        """
        return self._campaign_status

    @campaign_status.setter
    def campaign_status(self, campaign_status):
        """Sets the campaign_status of this AdvertiserCampaignMessage.


        :param campaign_status: The campaign_status of this AdvertiserCampaignMessage.  # noqa: E501
        :type: str
        """

        self._campaign_status = campaign_status

    @property
    def status(self):
        """Gets the status of this AdvertiserCampaignMessage.  # noqa: E501


        :return: The status of this AdvertiserCampaignMessage.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AdvertiserCampaignMessage.


        :param status: The status of this AdvertiserCampaignMessage.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, AdvertiserCampaignMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other