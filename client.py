# test_client.py
import asyncio
from fastmcp import Client
import json


async def main():
    async with Client("http://127.0.0.1:8001/mcp") as client:
        single = await client.call_tool("get_objects_by_ids_using_adk_agent")
        print("Fetched single:", single)
        

if __name__ == "__main__":
    asyncio.run(main())
