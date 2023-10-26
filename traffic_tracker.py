from browsermobproxy import Server
from selenium import webdriver

# Path to BrowserMob Proxy binary
bmp_path = "path/to/browsermob-proxy-2.1.4/bin/browsermob-proxy"

# Start BrowserMob Proxy server
server = Server(bmp_path)
server.start()
proxy = server.create_proxy()

# Configure Selenium to use the proxy
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={proxy.proxy}")

# Start Chrome
driver = webdriver.Chrome(options=chrome_options)

# Start capturing network traffic
proxy.new_har("example")

# Navigate to a website
driver.get("http://example.com")

# Stop capturing network traffic
result = proxy.har

# Save the result to a file
with open("output.har", "w") as f:
    f.write(str(result))

# Stop Selenium and the proxy server
driver.quit()
server.stop()
