import requests


class DomainsService:
    URL_PHISHING_API = "https://dnstwister.report/api/fuzz/"
    URL_DOMAIN_TO_HEXA_API = "https://dnstwister.report/api/to_hex/"
    URL_IP_API = "https://dnstwister.report/api/ip/"
    URL_LOCATION_API = "http://ip-api.com/json/"
    URL_MX_API = "https://dnstwister.report/api/mx/"

    @staticmethod
    def handle_request_errors(response):
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            return {"error": f"Request error: {err}"}

    @staticmethod
    async def make_get_request(url: str) -> dict:
        response = requests.get(url)
        return DomainsService.handle_request_errors(response)

    @staticmethod
    async def convert_to_hexadecimal(domain: str) -> str:
        url = DomainsService.URL_DOMAIN_TO_HEXA_API + domain
        response_dict = await DomainsService.make_get_request(url)
        return response_dict.get("domain_as_hexadecimal")

    @staticmethod
    async def find_data_by_domain(domain: str) -> dict:
        url = DomainsService.URL_DOMAIN_TO_HEXA_API + domain
        response_dict = await DomainsService.make_get_request(url)
        return response_dict

    @staticmethod
    async def find_all_phishing_sites_by_domain(domain: str) -> list:
        hexadecimal = await DomainsService.convert_to_hexadecimal(domain)
        url = DomainsService.URL_PHISHING_API + hexadecimal
        response_dict = await DomainsService.make_get_request(url)
        return response_dict.get("fuzzy_domains", [])

    @staticmethod
    async def find_all_phishing_sites_by_domain_hexadecimal(hexadecimal: str) -> dict:
        url = DomainsService.URL_PHISHING_API + hexadecimal
        response_dict = await DomainsService.make_get_request(url)
        return response_dict

    @staticmethod
    async def find_ip_by_domain(domain: str) -> str:
        hexadecimal = await DomainsService.convert_to_hexadecimal(domain)
        url = DomainsService.URL_IP_API + hexadecimal
        response_dict = await DomainsService.make_get_request(url)
        return response_dict.get("ip")

    @staticmethod
    async def find_location_by_ip(ip: str) -> dict:
        url = DomainsService.URL_LOCATION_API + ip + "?fields=continent,country,regionName,city,zip,lat,lon,timezone,currency,isp,org,reverse,mobile,proxy,hosting,query"
        response_dict = await DomainsService.make_get_request(url)
        return response_dict

    @staticmethod
    async def find_location_by_domain(domain: str) -> dict:
        ip = await DomainsService.find_ip_by_domain(domain)
        if ip:
            return await DomainsService.find_location_by_ip(ip)
        else:
            return {"error": "No IP found"}

    @staticmethod
    async def find_if_domain_is_available(domain: str) -> bool:
        url = DomainsService.URL_MX_API + await DomainsService.convert_to_hexadecimal(domain)
        response_dict = await DomainsService.make_get_request(url)
        if not response_dict.get("mx"):
            return True
        else:
            return False
