import os
from datetime import datetime


class FailureHandler:

    @staticmethod
    def capture(driver, test_name):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        os.makedirs("screenshots", exist_ok=True)
        os.makedirs("page_sources", exist_ok=True)
        os.makedirs("console_logs", exist_ok=True)

        # Screenshot
        screenshot_path = (
            f"screenshots/{test_name}_{timestamp}.png"
        )

        driver.save_screenshot(screenshot_path)

        # Page source
        source_path = (
            f"page_sources/{test_name}_{timestamp}.html"
        )

        with open(source_path, "w", encoding="utf-8") as file:
            file.write(driver.page_source)

        # Browser console logs
        try:
            logs = driver.get_log("browser")

            console_path = (
                f"console_logs/{test_name}_{timestamp}.log"
            )

            with open(console_path, "w", encoding="utf-8") as file:
                for log in logs:
                    file.write(f"{log}\n")

        except Exception:
            pass

        return {
            "screenshot": screenshot_path,
            "page_source": source_path
        }