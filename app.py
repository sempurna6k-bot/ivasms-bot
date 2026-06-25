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
                '--disable-web-security'
            ]
        )
        
        page = await browser.new_page()
        
        # Stealth headers
        await page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        })

        print("🔑 Membuka halaman login...")
        await page.goto("https://www.ivasms.com/login", timeout=120000, wait_until="domcontentloaded")
        
        await asyncio.sleep(12)  # Tunggu lebih lama

        # Diagnostic
        title = await page.title()
        print(f"📄 Page Title: {title}")
        
        content = await page.content()
        if "Cloudflare" in content or "checking your browser" in content.lower():
            print("❌ Cloudflare Challenge Detected!")
        else:
            print("✅ Tidak terdeteksi Cloudflare")

        # Coba cari input dengan berbagai cara
        try:
            await page.wait_for_selector('input[name="email"], input[type="email"]', timeout=30000)
            await page.fill('input[name="email"]', EMAIL)
            await page.fill('input[name="password"]', PASSWORD)
            print("✅ Form berhasil diisi")
            
            await page.click('button[type="submit"], button:contains("Login")')
            print("✅ Tombol login diklik")
            
            await asyncio.sleep(10)
            print("Current URL:", page.url)
            
        except Exception as e:
            print("❌ Error saat login:", str(e))
            await page.screenshot(path="login_error.png")
            print("📸 Screenshot error disimpan")

        # Keep alive
        while True:
            print(f"✅ Bot masih hidup - {datetime.now().strftime('%H:%M:%S')}")
            await asyncio.sleep(30)

asyncio.run(main())
