# ValidateSuccessTokenRequest


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `app_id`                                         | *str*                                            | :heavy_check_mark:                               | Uuid of the OnlyAuth App (APPX-XXX)              |
| `client_id`                                      | *str*                                            | :heavy_check_mark:                               | Uuid of you in the OnlyAuth Platform  (CLNT-XXX) |
| `token`                                          | *str*                                            | :heavy_check_mark:                               | The success token to be validated (TOKN-XXX)     |