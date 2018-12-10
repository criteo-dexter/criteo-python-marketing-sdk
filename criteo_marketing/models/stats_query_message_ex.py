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


class StatsQueryMessageEx(object):
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
        'report_type': 'str',
        'ignore_x_device': 'bool',
        'advertiser_ids': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'dimensions': 'list[str]',
        'metrics': 'list[str]',
        'format': 'str',
        'currency': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'report_type': 'reportType',
        'ignore_x_device': 'ignoreXDevice',
        'advertiser_ids': 'advertiserIds',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'dimensions': 'dimensions',
        'metrics': 'metrics',
        'format': 'format',
        'currency': 'currency',
        'timezone': 'timezone'
    }

    def __init__(self, report_type=None, ignore_x_device=None, advertiser_ids=None, start_date=None, end_date=None, dimensions=None, metrics=None, format=None, currency=None, timezone=None):  # noqa: E501
        """StatsQueryMessageEx - a model defined in OpenAPI"""  # noqa: E501

        self._report_type = None
        self._ignore_x_device = None
        self._advertiser_ids = None
        self._start_date = None
        self._end_date = None
        self._dimensions = None
        self._metrics = None
        self._format = None
        self._currency = None
        self._timezone = None
        self.discriminator = None

        if report_type is not None:
            self.report_type = report_type
        if ignore_x_device is not None:
            self.ignore_x_device = ignore_x_device
        if advertiser_ids is not None:
            self.advertiser_ids = advertiser_ids
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if dimensions is not None:
            self.dimensions = dimensions
        if metrics is not None:
            self.metrics = metrics
        if format is not None:
            self.format = format
        if currency is not None:
            self.currency = currency
        if timezone is not None:
            self.timezone = timezone

    @property
    def report_type(self):
        """Gets the report_type of this StatsQueryMessageEx.  # noqa: E501


        :return: The report_type of this StatsQueryMessageEx.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this StatsQueryMessageEx.


        :param report_type: The report_type of this StatsQueryMessageEx.  # noqa: E501
        :type: str
        """
        allowed_values = ["CampaignPerformance", "FacebookDPA", "TransactionID"]  # noqa: E501
        if report_type not in allowed_values:
            print("Unknown value `report_type` [{0}]".format(report_type))

        self._report_type = report_type

    @property
    def ignore_x_device(self):
        """Gets the ignore_x_device of this StatsQueryMessageEx.  # noqa: E501


        :return: The ignore_x_device of this StatsQueryMessageEx.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_x_device

    @ignore_x_device.setter
    def ignore_x_device(self, ignore_x_device):
        """Sets the ignore_x_device of this StatsQueryMessageEx.


        :param ignore_x_device: The ignore_x_device of this StatsQueryMessageEx.  # noqa: E501
        :type: bool
        """

        self._ignore_x_device = ignore_x_device

    @property
    def advertiser_ids(self):
        """Gets the advertiser_ids of this StatsQueryMessageEx.  # noqa: E501


        :return: The advertiser_ids of this StatsQueryMessageEx.  # noqa: E501
        :rtype: str
        """
        return self._advertiser_ids

    @advertiser_ids.setter
    def advertiser_ids(self, advertiser_ids):
        """Sets the advertiser_ids of this StatsQueryMessageEx.


        :param advertiser_ids: The advertiser_ids of this StatsQueryMessageEx.  # noqa: E501
        :type: str
        """

        self._advertiser_ids = advertiser_ids

    @property
    def start_date(self):
        """Gets the start_date of this StatsQueryMessageEx.  # noqa: E501


        :return: The start_date of this StatsQueryMessageEx.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this StatsQueryMessageEx.


        :param start_date: The start_date of this StatsQueryMessageEx.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this StatsQueryMessageEx.  # noqa: E501


        :return: The end_date of this StatsQueryMessageEx.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this StatsQueryMessageEx.


        :param end_date: The end_date of this StatsQueryMessageEx.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def dimensions(self):
        """Gets the dimensions of this StatsQueryMessageEx.  # noqa: E501


        :return: The dimensions of this StatsQueryMessageEx.  # noqa: E501
        :rtype: list[str]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this StatsQueryMessageEx.


        :param dimensions: The dimensions of this StatsQueryMessageEx.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["CampaignId", "AdvertiserId", "Category", "Seller", "Hour", "Day", "Week", "Month", "Year"]  # noqa: E501
        if not set(dimensions).issubset(set(allowed_values)):
            print("Unknown value `dimensions` [{0}]".format(dimensions))

        self._dimensions = dimensions

    @property
    def metrics(self):
        """Gets the metrics of this StatsQueryMessageEx.  # noqa: E501


        :return: The metrics of this StatsQueryMessageEx.  # noqa: E501
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this StatsQueryMessageEx.


        :param metrics: The metrics of this StatsQueryMessageEx.  # noqa: E501
        :type: list[str]
        """

        self._metrics = metrics

    @property
    def format(self):
        """Gets the format of this StatsQueryMessageEx.  # noqa: E501


        :return: The format of this StatsQueryMessageEx.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this StatsQueryMessageEx.


        :param format: The format of this StatsQueryMessageEx.  # noqa: E501
        :type: str
        """
        allowed_values = ["Csv", "Excel", "Xml", "Json"]  # noqa: E501
        if format not in allowed_values:
            print("Unknown value `format` [{0}]".format(format))

        self._format = format

    @property
    def currency(self):
        """Gets the currency of this StatsQueryMessageEx.  # noqa: E501


        :return: The currency of this StatsQueryMessageEx.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this StatsQueryMessageEx.


        :param currency: The currency of this StatsQueryMessageEx.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def timezone(self):
        """Gets the timezone of this StatsQueryMessageEx.  # noqa: E501


        :return: The timezone of this StatsQueryMessageEx.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this StatsQueryMessageEx.


        :param timezone: The timezone of this StatsQueryMessageEx.  # noqa: E501
        :type: str
        """
        allowed_values = ["GMT", "PST", "JST"]  # noqa: E501
        if timezone not in allowed_values:
            print("Unknown value `timezone` [{0}]".format(timezone))

        self._timezone = timezone

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
        if not isinstance(other, StatsQueryMessageEx):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
