# Authentication
(*authentication*)

### Available Operations

* [create_access_token](#create_access_token) - Creates a short-lived JWT token to integrate the widget
* [validate_success_token](#validate_success_token) - Validates a success token after user completes authentication

## create_access_token

Creates a short-lived JWT token to integrate the widget

### Example Usage

```python
import onlyauth
from onlyauth.models import operations

s = onlyauth.Onlyauth(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.authentication.create_access_token(request=operations.CreateAccessTokenRequestBody(
    app_id='<value>',
    client_id='<value>',
    end_user_phone_number='<value>',
    end_user_uuid='<value>',
    redirect_uri='<value>',
    language='<value>',
    region='<value>',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateAccessTokenRequestBody](../../models/operations/createaccesstokenrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.CreateAccessTokenResponse](../../models/operations/createaccesstokenresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400,401              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |

## validate_success_token

Validates a success token after user completes authentication

### Example Usage

```python
import onlyauth

s = onlyauth.Onlyauth(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.authentication.validate_success_token(app_id='<value>', client_id='<value>', token='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `app_id`                                         | *str*                                            | :heavy_check_mark:                               | Uuid of the OnlyAuth App (APPX-XXX)              |
| `client_id`                                      | *str*                                            | :heavy_check_mark:                               | Uuid of you in the OnlyAuth Platform  (CLNT-XXX) |
| `token`                                          | *str*                                            | :heavy_check_mark:                               | The success token to be validated (TOKN-XXX)     |


### Response

**[operations.ValidateSuccessTokenResponse](../../models/operations/validatesuccesstokenresponse.md)**
### Errors

| Error Object         | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400,401              | application/json     |
| errors.SDKError      | 4xx-5xx              | */*                  |
