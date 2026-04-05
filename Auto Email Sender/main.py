import asyncio
from agents import Runner, trace
from app_agents import sales_manager

message = "Send out a cold sales email addressed to Dear CEO from Alice"

async def main():
    with trace("Protected Automated SDR"):
        result = await Runner.run(sales_manager, message)
        return result

if __name__ == "__main__":
    asyncio.run(main())