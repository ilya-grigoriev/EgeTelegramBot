import pyppeteer
import asyncio
from loguru import logger
import traceback
import re


async def make_screenshot(*, file_path_for_open: str,
                          file_path_for_save: str) -> None:
    try:
        browser = await pyppeteer.launch(
            {'--headless': True, '--start-maxsized': False})
        page = await browser.newPage()

        logger.info('Starting to take screenshot...')

        options = {'waitUntil': 'domcontentloaded'}
        await page.goto(fr"file:{file_path_for_open}", options=options)

        html_code = await page.content()
        check_mathjax = re.search('<math>', html_code)
        if check_mathjax:
            options_for_search = {'timeout': 5000}
            try:
                await page.waitForXPath(
                    '//span[@class="math"]',
                    options=options_for_search)
                await page.waitForXPath('//span[@class="semantics"]',
                                        options=options_for_search)
                await page.waitForXPath('//nobr', options=options_for_search)
                await page.waitForXPath('//span[@class="mrow"]',
                                        options=options_for_search)
            except pyppeteer.errors.TimeoutError:
                logger.error(traceback.format_exc())
                logger.error(f'File: {file_path_for_open}')

        check_img = await page.xpath('//img')
        if check_img:
            await asyncio.sleep(1)

        await page.screenshot({"path": file_path_for_save})

        await browser.close()
        logger.info('Screenshot taken')
    except Exception:
        logger.error(traceback.format_exc())


if __name__ == '__main__':
    asyncio.run(make_screenshot(
        file_path_for_open=r'C:\Users\ilia0\PycharmProjects\EgeTelegramBot\parse_data\test.html',
        file_path_for_save=r'C:\Users\ilia0\PycharmProjects\EgeTelegramBot\parse_data\test_2.png'))
