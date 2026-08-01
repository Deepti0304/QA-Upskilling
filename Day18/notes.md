# Window Handles

Every browser window has a unique ID called Window Handle.

Methods

driver.current_window_handle
driver.window_handles
driver.switch_to.window()
driver.close()
driver.quit()

Difference between close() and quit()

Window Switching Flow

Parent
↓

Click link
↓

Child opens
↓

Switch to child
↓

Validate
↓

Close child
↓

Switch back
↓

Validate parent

Interview Questions

What is a Window Handle?

Difference between close() and quit()?

Difference between current_window_handle and window_handles?

How do you switch to a child window?

Why save parent handle?

