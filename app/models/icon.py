from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from app import constants

# icon_service = IconService(HTTPProvider("http://127.0.0.1:9000/api/v3"))
icon_service = IconService (HTTPProvider (constants.HTTP_PROVIDER))
