from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.controllers.DomainsController import DomainsController

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


class InvalidDomainFormat(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Invalid domain format. Domain name must be a string.")


class DomainNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Domain not found.")


@app.exception_handler(InvalidDomainFormat)
async def invalid_domain_format_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


@app.exception_handler(DomainNotFoundError)
async def domain_not_found_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"}
    )


@app.get("/api/domains/{domain}")
async def find_phishing_sites_by_domain(domain: str):
    if not isinstance(domain, str):
        raise InvalidDomainFormat()
    result = await DomainsController.find_phishing_domains_by_domain_name(domain)
    if not result:
        raise DomainNotFoundError()
    return result


@app.get("/api/domain/{domain}")
async def find_data_by_domain(domain: str):
    if not isinstance(domain, str):
        raise InvalidDomainFormat()
    result = await DomainsController.find_data_by_domain(domain)
    if not result:
        raise DomainNotFoundError()
    return result


@app.get("/api/ip/{domain}")
async def find_ip_by_domain(domain: str):
    if not isinstance(domain, str):
        raise InvalidDomainFormat()
    result = await DomainsController.find_ip_by_domain(domain)
    if not result:
        raise DomainNotFoundError()
    return result


@app.get("/api/location/{domain}")
async def find_location_by_domain(domain: str):
    if not isinstance(domain, str):
        raise InvalidDomainFormat()
    result = await DomainsController.find_location_by_domain(domain)
    if not result:
        raise DomainNotFoundError()
    return result


@app.get("/api/available/{domain}")
async def find_if_domain_is_available(domain: str):
    if not isinstance(domain, str):
        raise InvalidDomainFormat()
    return await DomainsController.find_if_domain_is_available(domain)
