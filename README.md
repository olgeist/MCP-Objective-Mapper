# MCP-Objective-Mapper

Here is the README.md documentation for your extension. You can save this text directly into a README.md file in your repository.
# Auto Button Selector & Shortcut Mapper
A lightweight browser extension (Chrome, Edge, Brave) that allows you to dynamically assign keyboard shortcuts to any clickable element on a webpage. Perfect for power users, data entry, and repetitive tasks where using a mouse slows you down.
## 💡 Use Cases
 * **High-Speed Data Entry:** Quickly map "Submit", "Next", or "Approve" buttons to single keystrokes so you never have to move your hands from the keyboard.
 * **Repetitive Workflow Automation:** Assign custom keys to buried UI elements on complex dashboards (like Jira, Salesforce, or AWS) for instant access.
 * **Accessibility & Ergonomics:** Navigate dense webpages effortlessly without relying on a mouse or trackpad.
 * **Web Testing & Scraping Prep:** Use the visual badge mapping to quickly identify clickable DOM targets and their properties across different browser DevTools.
## 🚀 Deployment & Installation
Because this is a custom extension, it is installed locally via "Developer Mode" in your Chromium-based browser.
 1. Download or clone this repository to your local machine.
 2. Open your browser and navigate to the extensions page:
   * **Chrome / Brave:** chrome://extensions/
   * **Edge:** edge://extensions/
 3. Toggle **Developer mode** ON (usually located in the top-right corner).
 4. Click the **Load unpacked** button.
 5. Select the auto-button-selector folder containing the manifest.json file.
 6. The extension is now active and will inject into any newly loaded webpage.
## How to Use
The extension operates entirely via keyboard shortcuts. Once loaded on a page, use the following commands:
 * **Alt + M (Auto-Map):** Instantly scans the page for standard buttons (<button>, [role="button"], etc.) and assigns them a numbered shortcut (1, 2, 3...).
 * **Alt + S (Inspector Mode):** Toggles manual target selection. Hover your mouse over *any* specific element on the page (it will highlight with a red dashed box) and press **any single key** (e.g., A-Z, 0-9) to bind that key to the element.
 * **Trigger a Click:** Simply press the assigned alphanumeric key to trigger the click event on the bound button. *(Note: Shortcuts will not trigger if your cursor is actively inside a text input field).*
 * **Alt + C (Clear All):** Removes all active shortcuts and visual badges from the current page.
## 🛠️ Testing Environment
If you deployed the test script (index.html) to GitHub Pages, you can use it as a safe sandbox:
 1. Navigate to your live GitHub Pages URL (e.g., https://[your-username].github.io/button-extension-test/).
 2. Press Alt + M to see the standard buttons light up with badges.
 3. Press 1, 2, or 3 and watch the built-in console log verify the simulated clicks.
 4. Press Alt + S, hover over the custom div elements, assign the key X, and press X to trigger it.
