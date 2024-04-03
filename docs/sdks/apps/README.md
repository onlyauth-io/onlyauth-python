# Apps
(*apps*)

### Available Operations

* [get_apps](#get_apps) - Get all apps
* [new_app](#new_app) - Create a new app
* [delete_app](#delete_app) - Delete an app
* [get_app_by_id](#get_app_by_id) - Get an app by uuid
* [update_app](#update_app) - Update an app

## get_apps

Get all apps

### Example Usage

```python
import onlyauth

s = onlyauth.Onlyauth(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.apps.get_apps(client_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                       | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `client_id`                                     | *str*                                           | :heavy_check_mark:                              | Uuid of you in the OnlyAuth Platform (CLNT-XXX) |


### Response

**[operations.GetAppsResponse](../../models/operations/getappsresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400,401              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## new_app

Create a new app

### Example Usage

```python
import onlyauth
from onlyauth.models import operations

s = onlyauth.Onlyauth(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.NewAppRequestBody()

res = s.apps.new_app(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.NewAppRequestBody](../../models/operations/newapprequestbody.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.NewAppResponse](../../models/operations/newappresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400,401              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## delete_app

Delete an app

### Example Usage

```python
import onlyauth

s = onlyauth.Onlyauth(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.apps.delete_app(app_id='<value>', client_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `app_id`                                              | *str*                                                 | :heavy_check_mark:                                    | Unique identifier of the app to be deleted (APPX-XXX) |
| `client_id`                                           | *str*                                                 | :heavy_check_mark:                                    | Client identifier for authentication (CLNT-XXX)       |


### Response

**[operations.DeleteAppResponse](../../models/operations/deleteappresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400,401              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## get_app_by_id

Get an app by uuid

### Example Usage

```python
import onlyauth

s = onlyauth.Onlyauth(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.apps.get_app_by_id(app_id='<value>', client_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `app_id`                                              | *str*                                                 | :heavy_check_mark:                                    | Unique identifier of the app to be fetched (APPX-XXX) |
| `client_id`                                           | *str*                                                 | :heavy_check_mark:                                    | Client identifier for authentication (CLNT-XXX)       |


### Response

**[operations.GetAppByIDResponse](../../models/operations/getappbyidresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400,401              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## update_app

Update an app

### Example Usage

```python
import onlyauth
from onlyauth.models import operations

s = onlyauth.Onlyauth(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.apps.update_app(app_id='<value>', client_id='<value>', request_body=operations.UpdateAppRequestBody())

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `app_id`                                                                           | *str*                                                                              | :heavy_check_mark:                                                                 | Unique identifier of the app to be updated (APPX-XXX)                              |
| `client_id`                                                                        | *str*                                                                              | :heavy_check_mark:                                                                 | Client identifier for authentication (CLNT-XXX)                                    |
| `request_body`                                                                     | [operations.UpdateAppRequestBody](../../models/operations/updateapprequestbody.md) | :heavy_check_mark:                                                                 | N/A                                                                                |


### Response

**[operations.UpdateAppResponse](../../models/operations/updateappresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400,401              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |
