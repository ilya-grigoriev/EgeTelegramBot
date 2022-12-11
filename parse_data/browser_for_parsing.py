import pyppeteer
import asyncio
from loguru import logger
import traceback


async def make_screenshot(*, file_path_for_open: str,
                          file_path_for_save: str) -> None:
    try:
        browser = await pyppeteer.launch(
            {'--headless': True, '--start-maxsized': False})
        page = await browser.newPage()

        logger.info('Starting to take screenshot...')
        await page.goto(fr"file:{file_path_for_open}")
        await asyncio.sleep(3)
        await page.screenshot({"path": file_path_for_save})
        await browser.close()
        logger.info('Screenshot taken')
    except Exception:
        logger.error(traceback.format_exc())
