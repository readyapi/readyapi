import subprocess
import time

import httpx
from playwright.sync_api import Playwright, sync_playwright


# Run playwright codegen to generate the code below, copy paste the sections in run()
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    # Update the viewport manually
    context = browser.new_context(viewport={"width": 960, "height": 1080})
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8000/docs")
    page.get_by_role("button", name="GET /items/ Read Items").click()
    page.get_by_role("button", name="Try it out").click()
    page.get_by_role("heading", name="Servers").click()
    # Manually add the screenshot
    page.screenshot(path="docs/en/docs/img/tutorial/query-param-models/image01.png")

    # ---------------------
    context.close()
    browser.close()


process = subprocess.Popen(
    ["readyapi", "run", "examples/query_param_models/tutorial001.py"]
)
try:
    for _ in range(3):
        try:
            response = httpx.get("http://localhost:8000/docs")
        except httpx.ConnectError:
            time.sleep(1)
            break
    with sync_playwright() as playwright:
        run(playwright)
finally:
    process.terminate()
