import pyppeteer
import asyncio
from logger_for_project import my_logger
import traceback
import re


async def make_pdf(*, file_path_for_open: str, file_path_for_save: str) -> None:
    try:
        browser = await pyppeteer.launch({"--headless": True, "--start-maxsized": True})
        page = await browser.newPage()
        await page.setViewport(viewport={"width": 1920, "height": 1080})

        my_logger.info("Starting to create PDF...")

        options = {"waitUntil": "domcontentloaded"}
        await page.goto(rf"file:{file_path_for_open}", options=options)

        check_img = await page.xpath("//img")
        if check_img:
            await page.waitFor(5000)

        await page.pdf(path=file_path_for_save, printBackground=True)
        await browser.close()
        my_logger.success("PDF taken")
    except Exception as e:
        my_logger.error(e)


if __name__ == "__main__":
    for_open = r"C:\Users\ilia0\PycharmProjects\EgeTelegramBot\parse_data\convert\tests\test.html"
    for_save = r"C:\Users\ilia0\PycharmProjects\EgeTelegramBot\parse_data\convert\tests\test.pdf"
    asyncio.run(make_pdf(file_path_for_open=for_open, file_path_for_save=for_save))
