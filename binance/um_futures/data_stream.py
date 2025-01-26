from binance.lib.utils import check_required_parameter


def new_listen_key(self):
    """
    |
    | **Create a ListenKey (USER_STREAM)**

    :API endpoint: ``POST /papi/v1/um/listenKey``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream
    |
    """

    url_path = "/papi/v1/um/listenKey"
    return self.send_request("POST", url_path)


def renew_listen_key(self, listenKey: str):
    """
    |
    | **Ping/Keep-alive a ListenKey (USER_STREAM)**

    :API endpoint: ``PUT /papi/v1/um/listenKey``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream

    :parameter listenKey: string
    |
    """

    check_required_parameter(listenKey, "listenKey")
    url_path = "/papi/v1/um/listenKey"
    return self.send_request("PUT", url_path, {"listenKey": listenKey})


def close_listen_key(self, listenKey: str):
    """
    |
    | **Close a ListenKey (USER_STREAM)**

    :API endpoint: ``DELETE /papi/v1/um/listenKey``
    :API doc: https://developers.binance.com/docs/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream

    :parameter listenKey: string
    |
    """

    check_required_parameter(listenKey, "listenKey")
    url_path = "/papi/v1/um/listenKey"
    return self.send_request("DELETE", url_path, {"listenKey": listenKey})
