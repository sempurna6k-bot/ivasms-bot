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
        
        # Tambahan anti-detection
        await page.set_extra_http_headers({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        print("🔑 Membuka halaman login...")
        await page.goto("https://www.ivasms.com/login", timeout=90000, wait_until="domcontentloaded")
        
        # Tunggu lebih lama + cek Cloudflare
        await asyncio.sleep(8)
        
        # Cek apakah ada Cloudflare
        if await page.locator("text=Cloudflare").count() > 0 or await page.locator("text=Checking your browser").count() > 0:
            print("❌ Cloudflare detected! Bot terblokir.")
        else:
            print("✅ Halaman login terbuka")

        # Coba isi form dengan timeout lebih panjang
        try:
            await page.wait_for_selector('input[name="email"]', timeout=30000)
            await page.fill('input[name="email"]', EMAIL)
            await page.fill('input[name="password"]', PASSWORD)
            print("✅ Form diisi")
            
            await page.click('button[type="submit"]')
            print("✅ Tombol login diklik")
            
            await asyncio.sleep(10)
            print("✅ Login selesai. Cek URL sekarang:", page.url)
            
        except Exception as e:
            print("❌ Error saat isi form:", e)
            # Simpan screenshot untuk debug
            await page.screenshot(path="error_screenshot.png")
            print("📸 Screenshot disimpan (error_screenshot.png)")

        # Biar bot tetap hidup
        while True:
            print("✅ Bot masih berjalan -", datetime.now().strftime("%H:%M:%S"))
            await asyncio.sleep(30)

asyncio.run(main())
