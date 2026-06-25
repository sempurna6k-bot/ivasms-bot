from playwright.async_api import async_playwright
import asyncio
from datetime import datetime

BOT_TOKEN = '8804507148:AAEu8Ya9dsQ96jXru90wrWdYwnpk9MdIyHE'
CHAT_ID = '8804507148'
EMAIL = 'nitenittt@gmail.com'
PASSWORD = 'Probolinggo0#'

async def main():
    print("🚀 Bot mulai di Railway...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True, 
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
        )
        page = await browser.new_page()
        
        print("🔑 Mencoba login ke iVASMS...")
        await page.goto("https://www.ivasms.com/login", timeout=90000)
        
        await page.fill('input[name="email"]', EMAIL)
        await page.fill('input[name="password"]', PASSWORD)
        await page.click('button[type="submit"]')
        
        await asyncio.sleep(10)
        print("✅ Login selesai!")

        # Test buka halaman SMS
        await page.goto("https://www.ivasms.com/portal/sms/received", timeout=60000)
        print("✅ Halaman SMS berhasil dibuka!")
        print("🕒 Test berhasil pada:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Biar bot tetap jalan
        while True:
            print("✅ Bot masih berjalan -", datetime.now().strftime("%H:%M:%S"))
            await asyncio.sleep(30)

asyncio.run(main())
