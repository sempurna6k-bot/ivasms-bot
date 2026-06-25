from playwright.async_api import async_playwright
import asyncio
import telegram
from datetime import datetime

BOT_TOKEN = '8804507148:AAEu8Ya9dsQ96jXru90wrWdYwnpk9MdIyHE'
CHAT_ID = '8804507148'
EMAIL = 'nitenittt@gmail.com'
PASSWORD = 'Probolinggo0#'

last = ""

async def kirim(sender, pesan):
    global last
    try:
        bot = telegram.Bot(token=BOT_TOKEN)
        teks = f"""📩 <b>SMS Baru</b>

📱 <b>Pengirim:</b> {sender}
💬 <b>Pesan:</b> {pesan}

🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""
        
        await bot.send_message(chat_id=CHAT_ID, text=teks, parse_mode='HTML')
        print(f"✅ Terkirim: {sender}")
        last = sender + pesan[:60]
    except Exception as e:
        print("Telegram error:", e)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("🔑 Login ke iVASMS...")
        await page.goto("https://www.ivasms.com/login", timeout=60000)
        await page.fill('input[name="email"]', EMAIL)
        await page.fill('input[name="password"]', PASSWORD)
        await page.click('button[type="submit"]')
        
        await asyncio.sleep(10)
        print("✅ Login berhasil, monitoring SMS...")

        while True:
            try:
                await page.goto("https://www.ivasms.com/portal/sms/received", timeout=60000)
                await asyncio.sleep(6)
                
                rows = await page.query_selector_all("tr")
                for row in rows[:10]:
                    try:
                        cells = await row.query_selector_all("td")
                        if len(cells) >= 2:
                            sender = (await cells[0].inner_text()).strip()
                            pesan = (await cells[1].inner_text()).strip()
                            key = sender + pesan[:60]
                            if pesan and key != last:
                                await kirim(sender, pesan)
                                last = key
                    except:
                        continue
            except Exception as e:
                print("Error:", e)
            
            await asyncio.sleep(12)

if __name__ == "__main__":
    asyncio.run(main())
