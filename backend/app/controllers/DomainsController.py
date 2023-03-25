from typing import List

from app.models.Domain import Domain
from app.services.DomainsService import DomainsService


class DomainsController:

    @staticmethod
    async def find_phishing_domains_by_domain_name(domain: str) -> list:
        return await DomainsService.find_all_phishing_sites_by_domain(domain)

    @staticmethod
    async def find_data_by_domain(domain: str) -> Domain:
        return await DomainsController.data_to_object(domain)

    @staticmethod
    async def find_location_by_domain(domain: str) -> dict:
        return await DomainsService.find_location_by_domain(domain)

    @staticmethod
    async def find_ip_by_domain(domain: str) -> str:
        return await DomainsService.find_ip_by_domain(domain)

    @staticmethod
    async def find_if_domain_is_available(domain: str) -> bool:
        return await DomainsService.find_if_domain_is_available(domain)

    @staticmethod
    async def find_all_phishing_sites_and_location_by_domain(domain: str) -> list[Domain]:
        sites = []
        phishing_sites = await DomainsService.find_all_phishing_sites_by_domain(domain)
        for site in phishing_sites:
            sites.append(await DomainsController.data_to_object(site))
        return sites

    @staticmethod
    async def data_to_object(domain_name: str) -> Domain:
        ip: str = await DomainsService.find_ip_by_domain(domain_name)
        available: bool = await DomainsService.find_if_domain_is_available(domain_name)
        location: [] = await DomainsService.find_location_by_domain(domain_name)

        return Domain(
            domain_name,
            ip,
            available,
            location
        )
