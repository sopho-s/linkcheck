import linkchecker
import asyncio
from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster
import threading
import installer

async def start_proxy():
    print("Initiating proxy...")
    opts = options.Options(listen_host="0.0.0.0", listen_port=1234)
    proxy = DumpMaster(opts)
    proxy.addons.add(linkchecker.Interceptor())
    try:
        print("Starting mitmproxy...")
        await proxy.run()  # Run inside the event loop
    except KeyboardInterrupt:
        print("Stopping mitmproxy...")
        proxy.shutdown()

def main():
    thread = threading.Thread(target=installer.installserver, args=(("0.0.0.0", 4321),)) 
    thread.start()
    asyncio.run(start_proxy())
    thread.join()


if __name__ == "__main__":
    main()