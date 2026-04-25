import linkchecker
import asyncio
from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster

async def start_proxy():
    opts = options.Options(listen_host="127.0.0.1", listen_port=8000)
    proxy = DumpMaster(opts)
    proxy.addons.add(linkchecker.Interceptor())

    try:
        print("Starting mitmproxy...")
        await proxy.run()  # Run inside the event loop
    except KeyboardInterrupt:
        print("Stopping mitmproxy...")
        proxy.shutdown()

def main():
    asyncio.run(start_proxy())


if __name__ == "__main__":
    main()