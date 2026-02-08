
    import asyncio
    from playwright.async_api import async_playwright
    
    async def cancel_subscription(target_name, login_url):
        print(f"🕵️ Assassin deploying to {target_name}...")
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False) # Headless=False so user can see the kill
            page = await browser.new_page()
            await page.goto(login_url)
            
            print("🕒 Waiting for user to log in manually...")
            print("   (Automatic login logic can be added to v2.0)")
            
            # This is where the 'Assassin' logic lives
            # We look for keywords: 'Cancel', 'Subscription', 'Settings', 'Billing'
            
            async def find_and_click(keywords):
                for word in keywords:
                    try:
                        element = page.get_by_role("button", name=word, exact=False)
                        if await element.is_visible():
                            await element.click()
                            print(f"✅ Clicked: {word}")
                            return True
                    except:
                        continue
                return False

            # Phase 1: Billing/Account
            await find_and_click(["Account", "Settings", "Billing", "Subscription"])
            
            # Phase 2: The Kill
            await find_and_click(["Cancel", "End Membership", "Stop Subscription"])
            
            # Phase 3: Handling the 'Dark Patterns'
            # We wait for the 'Stay for 50% off' or 'Are you sure?' popups
            time.sleep(2)
            await find_and_click(["Confirm", "Yes, Cancel", "Continue to cancel", "I still want to cancel"])
            
            print(f"🎯 Target {target_name} eliminated.")
            await browser.close()

    if __name__ == "__main__":
        # Example usage
        # asyncio.run(cancel_subscription("Generic Service", "https://example.com/login"))
        pass
    