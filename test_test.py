import asyncio

import pytest
from playwright.async_api import async_playwright, expect

loop: asyncio.AbstractEventLoop
headless = True


@pytest.mark.asyncio(loop_scope="function")
async def test_remember_loop():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='chrome', headless=headless)
        page = await browser.new_page()
        page.set_default_navigation_timeout(2000)
        await page.goto("http://playwright.dev")
        await page.get_by_text("Docs").click()
        await page.get_by_text('Getting started - VS Code').click()
        await expect(page.locator('h1')).to_have_text('Getting started - VS Code')


@pytest.mark.asyncio(loop_scope="module")
async def test_runs_in_a_loop():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='chrome', headless=headless)
        page = await browser.new_page()
        page.set_default_navigation_timeout(2000)
        await page.goto("http://playwright.dev")
        await page.get_by_text("Docs").click()
        await page.get_by_text('Getting started - VS Code').click()
        await expect(page.locator('h1')).to_have_text('Getting started - VS Code')
