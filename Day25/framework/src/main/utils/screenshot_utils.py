from pathlib import Path
from datetime import datetime


class ScreenshotUtils:

    @staticmethod
    def capture(driver, name="screenshot"):

        screenshot_dir = (
            Path(__file__).resolve()
            .parents[3]
            / "screenshots"
        )

        screenshot_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_path = (
            screenshot_dir /
            f"{name}_{timestamp}.png"
        )

        driver.save_screenshot(str(file_path))

        return str(file_path)