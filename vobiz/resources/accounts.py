# -*- coding: utf-8 -*-
"""
Vobiz Accounts resource.

Implements only the endpoints defined in the Vobiz accounts documentation.
"""

VOBIZ_API_V1 = "https://api.vobiz.ai/api/v1"


class Accounts:
    def __init__(self, client):
        self.client = client

    def get(self):
        """
        GET https://api.vobiz.ai/api/v1/auth/me
        """
        url = f"{VOBIZ_API_V1}/auth/me"
        resp = self.client.session.get(
            url, timeout=self.client.timeout, proxies=self.client.proxies
        )
        return self.client.process_response("GET", resp)

    def get_transactions(self, auth_id, limit=None, offset=None):
        """
        GET https://api.vobiz.ai/api/v1/account/{auth_id}/transactions
        """
        url = f"{VOBIZ_API_V1}/account/{auth_id}/transactions"
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        resp = self.client.session.get(
            url, params=params, timeout=self.client.timeout, proxies=self.client.proxies
        )
        return self.client.process_response("GET", resp)

    def get_balance(self, auth_id, currency):
        """
        GET https://api.vobiz.ai/api/v1/account/{auth_id}/balance/{currency}
        """
        url = f"{VOBIZ_API_V1}/account/{auth_id}/balance/{currency}"
        resp = self.client.session.get(
            url, timeout=self.client.timeout, proxies=self.client.proxies
        )
        return self.client.process_response("GET", resp)

    def get_concurrency(self, auth_id):
        """
        GET https://api.vobiz.ai/api/v1/account/{auth_id}/concurrency
        """
        url = f"{VOBIZ_API_V1}/account/{auth_id}/concurrency"
        resp = self.client.session.get(
            url, timeout=self.client.timeout, proxies=self.client.proxies
        )
        return self.client.process_response("GET", resp)

