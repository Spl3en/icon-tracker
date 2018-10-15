from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from app import constants

def get_icon_service (session):
    if not "nid" in session:
        session["nid"] = 0 # Mainnet

    nid = session["nid"]
    return IconService (HTTPProvider (constants.NETWORK_ENDPOINTS[nid]['url'] + "/api/v3"))
