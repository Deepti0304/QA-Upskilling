# Day 27 - Cross-Browser & Parallel Execution

## 1. Objective

The objective of Day 27 is to learn:

- Cross-browser testing
- Chrome, Firefox and Edge execution
- Browser factory
- pytest parameterization
- Parallel execution
- pytest-xdist
- Driver isolation
- Race conditions
- Execution time comparison
- Allure reporting for parallel execution

---

# 2. Cross-Browser Testing

Cross-browser testing means executing the same test cases against
different browsers.

Example:

- Chrome
- Firefox
- Edge

The test logic should remain the same.

Only the browser configuration changes.

Example:

test_login
    |
    +-- Chrome
    |
    +-- Firefox
    |
    +-- Edge

---

# 3. Why Cross-Browser Testing?

Different browsers may behave differently.

We test multiple browsers to verify:

- UI compatibility
- JavaScript behavior
- CSS rendering
- Browser-specific issues
- User experience
- Application functionality

---

# 4. Browser Factory

File:

src/main/utils/browser_factory.py

The Browser Factory is responsible for creating
the required Selenium WebDriver.

Example:

BrowserFactory.create_driver("chrome")

BrowserFactory.create_driver("firefox")

BrowserFactory.create_driver("edge")

Advantages:

- Centralized driver creation
- Less duplicate code
- Easy maintenance
- Easy to add new browsers
- Follows Factory Design Pattern

---

# 5. Supported Browsers

Day 27 supports:

- Chrome
- Firefox
- Edge

Example:

if browser == "chrome":
    webdriver.Chrome()

if browser == "firefox":
    webdriver.Firefox()

if browser == "edge":
    webdriver.Edge()

---

# 6. Configuration Management

Configuration should not be hardcoded in test files.

Bad:

driver.get("https://www.saucedemo.com/")

Good:

config = ConfigReader()

driver.get(config.get_base_url())

The URL is stored in:

resources/config.ini

---

# 7. config.ini

Example:

[environment]
base_url = https://www.saucedemo.com/

[browser]
default = chrome

[execution]
timeout = 10
headless = false

---

# 8. ConfigReader

File:

src/main/utils/config_reader.py

Responsibilities:

- Read config.ini
- Return application URL
- Return default browser
- Return timeout
- Return headless setting

Example:

config = ConfigReader()

url = config.get_base_url()

browser = config.get_default_browser()

timeout = config.get_timeout()

headless = config.is_headless()

---

# 9. Pytest Fixtures

File:

src/test/conftest.py

Fixtures are used to:

- Create WebDriver
- Open application
- Provide driver to tests
- Close browser after test

Basic flow:

Test
  |
  v
Fixture
  |
  v
Browser Factory
  |
  v
WebDriver
  |
  v
Test execution
  |
  v
driver.quit()

---

# 10. Browser Parameterization

pytest can execute the same test with different browsers.

Example:

@pytest.mark.parametrize(
    "driver",
    ["chrome", "firefox", "edge"],
    indirect=True
)

This means the test will execute three times.

Example:

test_login[chrome]

test_login[firefox]

test_login[edge]

---

# 11. indirect=True

indirect=True tells pytest to pass the parameter
to the fixture instead of directly to the test.

Example:

@pytest.mark.parametrize(
    "driver",
    ["chrome", "firefox", "edge"],
    indirect=True
)

The fixture receives:

request.param

Example:

def driver(request):

    browser = request.param

---

# 12. Parallel Execution

Parallel execution means running multiple tests
at the same time.

Sequential:

Test 1 -> 10 sec
Test 2 -> 10 sec
Test 3 -> 10 sec

Total:

30 sec

Parallel:

Test 1 -> 10 sec
Test 2 -> 10 sec
Test 3 -> 10 sec

Total:

Approximately 10-15 sec

Actual execution time depends on:

- CPU
- RAM
- Network
- Browser startup
- Number of tests
- Number of workers

---

# 13. pytest-xdist

pytest-xdist provides parallel test execution.

Install:

pip install pytest-xdist

Run:

pytest src/test -v -n 3

-n 3 means:

Use 3 workers.

---

# 14. Worker Concept

Example:

Worker 1 -> Test A

Worker 2 -> Test B

Worker 3 -> Test C

Each worker should have an independent WebDriver.

Do NOT share one WebDriver between workers.

---

# 15. Driver Isolation

Bad approach:

driver = webdriver.Chrome()

Multiple tests share the same driver.

This can cause:

- Test interference
- Race conditions
- Wrong browser state
- Incorrect URLs
- Session conflicts
- Unstable tests

Good approach:

Each test/worker gets its own driver.

Test A -> Driver A

Test B -> Driver B

Test C -> Driver C

---

# 16. Race Condition

A race condition occurs when multiple tests/processes
try to access or modify shared resources at the same time.

Example:

Test A changes URL

Test B changes URL

Both tests share the same browser.

Result:

Unpredictable behavior.

Solution:

Use isolated WebDriver instances.

---

# 17. ThreadLocal

In Java Selenium frameworks, ThreadLocal is commonly
used for parallel execution.

Example:

ThreadLocal<WebDriver>

Each thread gets its own WebDriver.

Important interview statement:

"In Java, I use ThreadLocal<WebDriver> to maintain
a separate WebDriver instance for each parallel thread."

In Python pytest, fixtures and pytest-xdist provide
a similar isolation approach.

---

# 18. Selenium Grid

Selenium Grid allows tests to execute on:

- Different browsers
- Different operating systems
- Different machines

Example:

Machine 1 -> Chrome

Machine 2 -> Firefox

Machine 3 -> Edge

This is useful for large test suites.

---

# 19. Local Parallel Execution vs Selenium Grid

Local parallel execution:

Tests run on the same machine.

Example:

Chrome
Firefox
Edge

Selenium Grid:

Tests can run across multiple machines/nodes.

Example:

Windows + Chrome

macOS + Safari

Linux + Firefox

---

# 20. Timing Comparison

First run sequentially:

time pytest src/test -v

Record:

Sequential Duration = ______ seconds

Then run parallel:

time pytest src/test -v -n 3

Record:

Parallel Duration = ______ seconds

Calculate:

Time Saved =
Sequential Duration - Parallel Duration

Improvement % =
((Sequential - Parallel) / Sequential) * 100

---

# 21. Example Timing Report

Sequential:

Duration = 60 seconds

Parallel:

Duration = 25 seconds

Time Saved:

35 seconds

Improvement:

58.33%

These are example values only.

Use actual execution results in the project.

---

# 22. Allure Reporting

Generate Allure results:

pytest src/test -v \
--alluredir=reports/allure-results

Generate report:

allure generate reports/allure-results \
-o reports/allure-report --clean

Open report:

allure open reports/allure-report

---

# 23. Parallel Allure Execution

Run:

pytest src/test -v -n 3 \
--alluredir=reports/allure-results

Then:

allure generate reports/allure-results \
-o reports/allure-report --clean

Open:

allure open reports/allure-report

---

# 24. Advantages of Parallel Execution

- Faster test execution
- Better CI/CD performance
- Faster regression testing
- Better utilization of CPU
- Useful for large test suites

---

# 25. Challenges of Parallel Execution

- Shared test data
- Shared files
- Database conflicts
- Driver sharing
- Race conditions
- Port conflicts
- Environment limitations
- Thread safety
- Test dependency

---

# 26. Best Practices

1. Keep tests independent.

2. Do not share WebDriver instances.

3. Avoid hardcoded URLs.

4. Keep configuration external.

5. Use fixtures for driver lifecycle.

6. Use unique test data where required.

7. Avoid test-to-test dependencies.

8. Capture screenshots for failures.

9. Generate reports.

10. Measure actual execution time.

---

# 27. Important Commands

Install xdist:

pip install pytest-xdist

Run normally:

pytest src/test -v

Run with 2 workers:

pytest src/test -v -n 2

Run with 3 workers:

pytest src/test -v -n 3

Run sequential timing:

time pytest src/test -v

Run parallel timing:

time pytest src/test -v -n 3

Generate Allure:

pytest src/test -v --alluredir=reports/allure-results

Generate Allure HTML:

allure generate reports/allure-results \
-o reports/allure-report --clean

Open Allure:

allure open reports/allure-report

---

# 28. Interview Questions

## Q1. What is cross-browser testing?

Cross-browser testing verifies that an application
works correctly across different browsers such as
Chrome, Firefox and Edge.

---

## Q2. Why do we need cross-browser testing?

Because browsers may differ in:

- Rendering
- JavaScript behavior
- CSS support
- Browser APIs
- Performance

---

## Q3. How do you implement cross-browser testing in pytest?

I use pytest parameterization with a browser fixture.

Example:

@pytest.mark.parametrize(
    "driver",
    ["chrome", "firefox", "edge"],
    indirect=True
)

---

## Q4. What is pytest-xdist?

pytest-xdist is a pytest plugin that allows tests
to execute in parallel across multiple workers.

---

## Q5. How do you run tests in parallel?

pytest src/test -v -n 3

---

## Q6. What does -n 3 mean?

It tells pytest-xdist to use three workers.

---

## Q7. Why should we not share WebDriver between parallel tests?

Sharing WebDriver can cause race conditions,
test interference and unpredictable browser state.

Each parallel test should have an isolated driver.

---

## Q8. What is ThreadLocal?

ThreadLocal provides a separate variable instance
for each thread.

In Java Selenium frameworks it is commonly used
to maintain separate WebDriver instances.

---

## Q9. What is Selenium Grid?

Selenium Grid allows Selenium tests to execute
on different machines, operating systems and browsers.

---

## Q10. What is the difference between parallel
execution and cross-browser testing?

Cross-browser testing means running tests against
different browsers.

Parallel execution means running multiple tests
at the same time.

They can be combined.

---

# 29. Day 27 Deliverables

The final Day 27 project should contain:

1. Browser Factory

2. Chrome execution

3. Firefox execution

4. Edge execution

5. pytest parameterization

6. Parallel execution using pytest-xdist

7. Isolated WebDriver instances

8. Sequential timing

9. Parallel timing

10. Allure report

11. Configuration externalized

12. notes.md

---

# 30. Final Architecture

Test
 |
 v
pytest
 |
 +-----------------------+
 |                       |
 v                       v
Chrome                 Firefox
 |                       |
 v                       v
WebDriver              WebDriver
 |
 +----------+
            |
            v
         Edge
            |
            v
         WebDriver

Configuration:

config.ini
    |
    v
ConfigReader
    |
    v
Test / Fixture

Browser creation:

Test
  |
  v
BrowserFactory
  |
  +-- Chrome
  +-- Firefox
  +-- Edge