import logging

import httpx
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from jwt.algorithms import RSAAlgorithm

from examples.mcp.shared.setup import setup_logging

setup_logging()

logger = logging.getLogger(__name__)


async def fetch_jwks_public_key(url: str) -> str:
    """
    Fetch JWKS from a given URL and extract the primary public key in PEM format.

    Args:
        url: The JWKS URL to fetch from

    Returns:
        PEM-formatted public key as a string
    """
    logger.info(f"Fetching JWKS from: {url}")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        jwks_data = response.json()

        if not jwks_data or "keys" not in jwks_data or not jwks_data["keys"]:
            logger.error("Invalid JWKS data format: missing or empty 'keys' array")
            raise ValueError("Invalid JWKS data format: missing or empty 'keys' array")

import json

async def fetch_jwks_public_key(url: str, *, kid: str | None = None) -> str:
    # ... (code that fetches jwks_data from the URL) ...

    if not jwks_data or "keys" not in jwks_data or not jwks_data["keys"]:
        logger.error("Invalid JWKS data format: missing or empty 'keys' array")
        raise ValueError("Invalid JWKS data format: missing or empty 'keys' array")

    keys = jwks_data["keys"]
    jwk = None
    if kid:
        jwk = next((k for k in keys if k.get("kid") == kid), None)
        if jwk is None:
            logger.warning("Requested kid not found in JWKS; attempting first key as fallback")
    if jwk is None:
        jwk = keys[0]

    # Convert JWK to PEM format
    public_key = RSAAlgorithm.from_jwk(json.dumps(jwk))
    if isinstance(public_key, RSAPublicKey):
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        pem_str = pem.decode("utf-8")
        logger.info("Successfully extracted public key from JWKS")
        return pem_str
    else:
        logger.error("Invalid JWKS data format: expected RSA public key")
        raise TypeError("Invalid JWKS data format: expected RSA public key")
            pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
            pem_str = pem.decode("utf-8")
            logger.info("Successfully extracted public key from JWKS")
            return pem_str
        else:
            logger.error("Invalid JWKS data format: expected RSA public key")
            raise ValueError("Invalid JWKS data format: expected RSA public key")
