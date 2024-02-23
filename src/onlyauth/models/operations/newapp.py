"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from onlyauth import utils
from typing import List, Optional


@dataclasses.dataclass
class NewAppRequestBody:
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'form': { 'field_name': 'client_id' }})
    r"""Client identifier"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class App:
    UNSET='__SPEAKEASY_UNSET__'
    sandbox_mode: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sandbox_mode') }})
    r"""Indicates if the app is in sandbox mode"""
    allow_sms_channel: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allow_sms_channel') }})
    r"""Indicates if SMS channel is allowed for guests"""
    icon: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('icon') }})
    r"""URL to the app's icon"""
    allow_totp_channel: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allow_totp_channel') }})
    r"""Indicates if TOTP channel is allowed for guests"""
    enabled: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled') }})
    r"""Indicates if the app is enabled"""
    app_domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_domain') }})
    r"""Domain of the app"""
    webauthn_enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webauthn_enabled') }})
    r"""Indicates if WebAuthn is enabled"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Uuid of the app (APPX-XXX)"""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Client identifier (CLNT-XXX)"""
    friendly_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('friendly_name'), 'exclude': lambda f: f is None }})
    r"""Friendly name of the app"""
    webauthn_redirect_allowed: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webauthn_redirect_allowed'), 'exclude': lambda f: f is App.UNSET }})
    r"""Indicates if WebAuthn redirect is allowed when webauthn_enabled is set to true"""
    supported_factors: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supported_factors'), 'exclude': lambda f: f is None }})
    r"""Supported factors for the app"""
    webauth_enabled: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webauth_enabled'), 'exclude': lambda f: f is App.UNSET }})
    r"""Indicates if WebAuth is enabled"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewAppResponseBody:
    r"""App created successfully"""
    app: Optional[List[App]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class NewAppResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[NewAppResponseBody] = dataclasses.field(default=None)
    r"""App created successfully"""
    

