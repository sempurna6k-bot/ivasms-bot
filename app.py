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
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-blink-features=AutomationControlled',
                '--disable-web-security',
                '--disable-features=VizDisplayCompositor'
            ]
        )
        
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        )
        
        page = await context.new_page()

        print("🔑 Membuka halaman login... (tunggu Cloudflare)")
        await page.goto("https://www.ivasms.com/login", timeout=120000, wait_until="domcontentloaded")
        
        await asyncio.sleep(15)   # Kasih waktu Cloudflare challenge

        title = await page.title()
        print(f"📄 Page Title: {title}")

        # Cek apakah form login muncul
        email_count = await page.locator('input[name="email"]').count()
        print(f"🔍 Input email ditemukan: {email_count}")

        if email_count > 0:
            print("✅ Form login muncul!")
            await page.fill('input[name="email"]', EMAIL)
            await page.fill('input[name="password"]', PASSWORD)
            await page.click('button[type="submit"]')
            print("✅ Login diklik")
            await asyncio.sleep(10)
        else:
            print("❌ Form login TIDAK muncul (masih Cloudflare)")

        # Keep alive
        while True:
            print(f"✅ Bot hidup - {datetime.now().strftime('%H:%M:%S')}")
            await asyncio.sleep(30)

asyncio.run(main())
