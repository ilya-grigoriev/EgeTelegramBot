"""This module help to run browser for parsing."""
import traceback

import pyppeteer
from logger_for_project import my_logger


async def make_pdf(*, file_path_for_open: str, file_path_for_save: str) -> None:
    """
    Make pdf file from html code.

    Parameters
    ----------
    file_path_for_open : str
        Existing file path for open file.
    file_path_for_save : str
        File path for save file.
    """
    try:
        options_for_browser = {"--headless": True, "--start-maxsized": True}
        browser = await pyppeteer.launch(options=options_for_browser)
        page = await browser.newPage()
        await page.setViewport(viewport={"width": 1920, "height": 1080})

        my_logger.info("Starting to create PDF...")

        options = {"waitUntil": "networkidle0"}
        await page.goto(rf"file:{file_path_for_open}", options=options)

        check_img = await page.xpath("//img")
        if check_img:
            await page.waitFor(1000)

        await page.pdf(path=file_path_for_save)
        await browser.close()
        my_logger.success("PDF taken")
    except Exception:
        my_logger.error(traceback.format_exc())
