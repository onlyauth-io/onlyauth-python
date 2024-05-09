<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->