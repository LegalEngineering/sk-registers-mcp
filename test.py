import asyncio
from server import hladaj_subjekt, detail_subjektu

async def test():
    print("=== TEST 1: hladaj_subjekt ===")
    result = await hladaj_subjekt(nazov="Welter")
    print(result)

asyncio.run(test())
