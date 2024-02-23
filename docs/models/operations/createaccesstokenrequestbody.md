# CreateAccessTokenRequestBody


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `app_id`                                        | *str*                                           | :heavy_check_mark:                              | Uuid of the OnlyAuth App (APPX-XXX)             |
| `client_id`                                     | *str*                                           | :heavy_check_mark:                              | Uuid of you in the OnlyAuth Platform (CLNT-XXX) |
| `end_user_phone_number`                         | *str*                                           | :heavy_check_mark:                              | Phone number of the end user (E164 format)      |
| `end_user_uuid`                                 | *str*                                           | :heavy_check_mark:                              | Uuid of the end user (any type)                 |
| `redirect_uri`                                  | *str*                                           | :heavy_check_mark:                              | URL to redirect to after authentication         |
| `language`                                      | *str*                                           | :heavy_check_mark:                              | Language code (e.g., en-US)                     |
| `region`                                        | *str*                                           | :heavy_check_mark:                              | Region code (us-1)                              |