import pyppeteer
import asyncio
from logger_for_project import my_logger
import traceback
import re


async def make_screenshot(*, file_path_for_open: str,
                          file_path_for_save: str) -> None:
    try:
        browser = await pyppeteer.launch(
            {'--headless': True, '--start-maxsized': False})
        page = await browser.newPage()

        my_logger.info('Starting to take screenshot...')

        options = {'waitUntil': 'domcontentloaded'}
        await page.goto(fr"file:{file_path_for_open}", options=options)

        html_code = await page.content()
        check_mathjax = re.search('<math>', html_code)
        if check_mathjax:
            options_for_search = {'timeout': 10000}
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
                my_logger.error(traceback.format_exc())
                my_logger.error(f'File: {file_path_for_open}')

        check_img = await page.xpath('//img')
        if check_img:
            await asyncio.sleep(2)

        await page.screenshot({"path": file_path_for_save})

        await browser.close()
        my_logger.info('Screenshot taken')
    except Exception:
        my_logger.error(traceback.format_exc())


if __name__ == '__main__':
    asyncio.run(make_screenshot(
        file_path_for_open=r'C:\Users\ilia0\PycharmProjects\EgeTelegramBot\parse_data\test.html',
        file_path_for_save=r'C:\Users\ilia0\PycharmProjects\EgeTelegramBot\parse_data\test_2.png'))
