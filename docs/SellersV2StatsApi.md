# criteo_marketing.SellersV2StatsApi

All URIs are relative to *https://api.criteo.com/marketing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**campaigns**](SellersV2StatsApi.md#campaigns) | **GET** /v2/crp/stats/campaigns | Get stats by campaign.
[**seller_campaigns**](SellersV2StatsApi.md#seller_campaigns) | **GET** /v2/crp/stats/seller-campaigns | Get stats by seller-campaign.
[**sellers**](SellersV2StatsApi.md#sellers) | **GET** /v2/crp/stats/sellers | Get stats by seller.


# **campaigns**
> str campaigns(authorization, interval_size=interval_size, click_attribution_policy=click_attribution_policy, start_date=start_date, end_date=end_date, campaign_id=campaign_id, count=count)

Get stats by campaign.

## Dimensions                Get performance statistics aggregated for _campaigns_. The campaign id appears  in the output as the first column.                Aggregation can be done by `hour`, `day`, `month`, or `year`. The aggregation  interval size is controlled by `intervalSize`. The time interval appears in  the output as the second column.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR = Conversion Rate | salesUnits / clicks  G | CPO = Cost Per Order | cost / salesUnits  H | COS = Cost of Sale | cost / revenue  I | ROAS = Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by `clickAttributionPolicy`.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by campaign, date or count.                Filtering the results to events associated with a specific campaign is done by setting  the `campaignId` filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the `startDate` and  `endDate` filter parameters using the `yyyy-MM-DD` format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is `hour`, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  `count` filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is `application/json` and  `text/csv`.                ```json  {     \"columns\": [ \"campaignId\", \"month\", \"impressions\", \"clicks\", \"cost\", \"saleUnits\", \"revenue\", \"cr\", \"cpo\", \"cos\", \"roas\" ],     \"data\": [         [168423, \"2019-05-01\", 3969032, 13410, 1111.295, 985, 190758099, 0.073, 1.128, 0.000, 171653.880 ],         [168423, \"2019-06-01\", 8479603, 25619, 2190.705, 740, 152783656, 0.028, 2.960, 0.000, 69741.775 ]         ],     \"rows\": 2  }  ```                The JSON result is an object with three fields (`columns`, `data`, and `rows`). The  “columns” array acts as the header for the data rows. The categorical dimension  column comes first and consists of the campaign id.  The interval column comes next and defines the aggregation period.  The interval size is  determined by the `intervalSize` parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining depend on the `clickAttributionPolicy` parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

* Api Key Authentication (Authorization): 
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = criteo_marketing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = criteo_marketing.SellersV2StatsApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
interval_size = 'interval_size_example' # str | Specify the aggregation interval for events used to compute stats (default is \"day\") (optional)
click_attribution_policy = 'click_attribution_policy_example' # str | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter out all events that occur before date (default is the value of `endDate`) (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter out all events that occur after date (default is today’s date) (optional)
campaign_id = 'campaign_id_example' # str | Show only metrics for this campaign (default all campaigns) (optional)
count = 56 # int | Return up to the first count rows of data (default is all rows) (optional)

try:
    # Get stats by campaign.
    api_response = api_instance.campaigns(authorization, interval_size=interval_size, click_attribution_policy=click_attribution_policy, start_date=start_date, end_date=end_date, campaign_id=campaign_id, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2StatsApi->campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **interval_size** | **str**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] 
 **click_attribution_policy** | **str**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] 
 **start_date** | **datetime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional] 
 **end_date** | **datetime**| Filter out all events that occur after date (default is today’s date) | [optional] 
 **campaign_id** | **str**| Show only metrics for this campaign (default all campaigns) | [optional] 
 **count** | **int**| Return up to the first count rows of data (default is all rows) | [optional] 

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seller_campaigns**
> str seller_campaigns(authorization, interval_size=interval_size, click_attribution_policy=click_attribution_policy, start_date=start_date, end_date=end_date, seller_id=seller_id, campaign_id=campaign_id, count=count)

Get stats by seller-campaign.

## Dimensions                Get performance statistics aggregated for _seller campaigns_.The campaign id, seller id, and  seller name appear in the first three columns of the output. These are followed by the interval  size column.                Aggregation can be done by `hour`, `day`, `month`, or `year`. The aggregation  interval size is controlled by `intervalSize`. The remaining columns are metrics.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR = Conversion Rate | salesUnits / clicks  G | CPO = Cost Per Order | cost / salesUnits  H | COS = Cost of Sale | cost / revenue  I | ROAS = Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by `clickAttributionPolicy`.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by date or count.                Filtering the results to events associated with a specific campaign is done by setting  the `campaignId` filter parameter to the desired value.                Filtering the results to events associated with a specific seller is done by setting  the `sellerId` filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the `startDate` and  `endDate` filter parameters using the `yyyy-MM-DD` format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is `hour`, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  `count` filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is `application/json` and  `text/csv`.                ```json  {      \"columns\": [          \"campaignId\", \"sellerId\", \"sellerName\", \"month\", \"impressions\", \"clicks\", \"cost\", \"saleUnits\", \"revenue\", \"cr\", \"cpo\", \"cos\", \"roas\"      ],      \"data\": [          [168423, 1110222, \"118883955\", \"2019-05-01\", 14542, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110222, \"118883955\", \"2019-06-01\", 16619, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110225, \"117980027\", \"2019-05-01\", 12502, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110225, \"117980027\", \"2019-06-01\", 20266, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0]      ],      \"rows\": 4  }  ```                The JSON result is an object with three fields (`columns`, `data`, and `rows`). The  “columns” array acts as the header for the data rows. The categorical dimension  columns come first and include the campaign id, seller id, and seller name.  The interval column comes next and defines the aggregation period. The interval size is  determined by the `intervalSize` parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining depend on the `clickAttributionPolicy` parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

* Api Key Authentication (Authorization): 
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = criteo_marketing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = criteo_marketing.SellersV2StatsApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
interval_size = 'interval_size_example' # str | Specify the aggregation interval for events used to compute stats (default is \"day\") (optional)
click_attribution_policy = 'click_attribution_policy_example' # str | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter out all events that occur before date (default is the value of `endDate`) (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter out all events that occur after date (default is today’s date) (optional)
seller_id = 'seller_id_example' # str | Show only metrics for this seller (default all sellers) (optional)
campaign_id = 'campaign_id_example' # str | Show only metrics for this campaign (default all campaigns) (optional)
count = 56 # int | Return up to the first count rows of data (default is all rows) (optional)

try:
    # Get stats by seller-campaign.
    api_response = api_instance.seller_campaigns(authorization, interval_size=interval_size, click_attribution_policy=click_attribution_policy, start_date=start_date, end_date=end_date, seller_id=seller_id, campaign_id=campaign_id, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2StatsApi->seller_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **interval_size** | **str**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] 
 **click_attribution_policy** | **str**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] 
 **start_date** | **datetime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional] 
 **end_date** | **datetime**| Filter out all events that occur after date (default is today’s date) | [optional] 
 **seller_id** | **str**| Show only metrics for this seller (default all sellers) | [optional] 
 **campaign_id** | **str**| Show only metrics for this campaign (default all campaigns) | [optional] 
 **count** | **int**| Return up to the first count rows of data (default is all rows) | [optional] 

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sellers**
> str sellers(authorization, interval_size=interval_size, click_attribution_policy=click_attribution_policy, start_date=start_date, end_date=end_date, seller_id=seller_id, count=count)

Get stats by seller.

## Dimensions                Get performance statistics aggregated for _sellers_. The seller id appears  in the output in the first column and the seller name appears in the second.                Aggregation can be done by `hour`, `day`, `month`, or `year`. The aggregation  interval size is controlled by `intervalSize`. The time interval appears in  the output as the second column.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR = Conversion Rate | salesUnits / clicks  G | CPO = Cost Per Order | cost / salesUnits  H | COS = Cost of Sale | cost / revenue  I | ROAS = Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by `clickAttributionPolicy`.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by seller id, date or count.                Filtering the results to events associated with a specific seller is done by setting  the `sellerId` filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the `startDate` and  `endDate` filter parameters using the `yyyy-MM-DD` format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is `hour`, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  `count` filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is `application/json` and  `text/csv`.                ```json  {      \"columns\": [\"sellerId\", \"sellerName\", \"month\", \"impressions\", \"clicks\", \"cost\", \"saleUnits\", \"revenue\", \"cr\", \"cpo\", \"cos\", \"roas\"],      \"data\": [         [1200972, \"sellerA\", \"2019-05-01\", 14542, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],         [1200972, \"sellerA\", \"2019-06-01\", 16619, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0],         [1200974, \"sellerB\", \"2019-05-01\", 10102, 47, 3.29, 3, 396000.0, 0.063, 1.096, 8.308E-6, 120364.741],         [1200974, \"sellerB\", \"2019-06-01\", 11576, 54, 3.78, 1, 132000.0, 0.018, 3.78, 2.863E-5, 34920.634]      ],      \"rows\": 4  }  ```                The JSON result is an object with three fields (`columns`, `data`, and `rows`). The  “columns” array acts as the header for the data rows. The categorical dimension  columns come first and include the seller id and seller name.  The interval column comes next and defines the aggregation period. The interval size is  determined by the `intervalSize` parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining metrics depend on the `clickAttributionPolicy` parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

* Api Key Authentication (Authorization): 
```python
from __future__ import print_function
import time
import criteo_marketing
from criteo_marketing.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = criteo_marketing.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = criteo_marketing.SellersV2StatsApi(criteo_marketing.ApiClient(configuration))
authorization = 'Bearer VALID_JWT_TOKEN_BASE64' # str | JWT Bearer Token (default to 'Bearer VALID_JWT_TOKEN_BASE64')
interval_size = 'interval_size_example' # str | Specify the aggregation interval for events used to compute stats (default is \"day\") (optional)
click_attribution_policy = 'click_attribution_policy_example' # str | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter out all events that occur before date (default is the value of `endDate`) (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter out all events that occur after date (default is today’s date) (optional)
seller_id = 'seller_id_example' # str | Show only metrics for this seller (default all sellers) (optional)
count = 56 # int | Return up to the first count rows of data (default is all rows) (optional)

try:
    # Get stats by seller.
    api_response = api_instance.sellers(authorization, interval_size=interval_size, click_attribution_policy=click_attribution_policy, start_date=start_date, end_date=end_date, seller_id=seller_id, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SellersV2StatsApi->sellers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| JWT Bearer Token | [default to &#39;Bearer VALID_JWT_TOKEN_BASE64&#39;]
 **interval_size** | **str**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] 
 **click_attribution_policy** | **str**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] 
 **start_date** | **datetime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional] 
 **end_date** | **datetime**| Filter out all events that occur after date (default is today’s date) | [optional] 
 **seller_id** | **str**| Show only metrics for this seller (default all sellers) | [optional] 
 **count** | **int**| Return up to the first count rows of data (default is all rows) | [optional] 

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
