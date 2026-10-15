import os

# Create directory
folder_name = "auto-button-selector"
os.makedirs(folder_name, exist_ok=True)

# 1. Manifest content
manifest_data = """{
  "manifest_version": 3,
  "name": "Auto Button Selector",
  "version": "1.0",
  "permissions": ["activeTab"],
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"],
      "css": ["styles.css"]
    }
  ]
}"""

# 2. Styles content
css_data = """
.abs-highlight { outline: 2px dashed #ff0055 !important; position: relative !important; }
.abs-shortcut-badge {
  position: absolute; top: -10px; right: -10px; background: #111827; color: #fff;
  font-family: monospace; font-size: 11px; padding: 2px 6px; border-radius: 4px; z-index: 999999;
}
"""

# 3. Content script content
js_data = """(function () {
  const shortcutMap = new Map();
  const keys = ["1","2","3","4","5","6","7","8","9","0","q","w","e","r"];
  let inspectMode = false, hovered = null;

  function attachBadge(el, key) {
    if (el.querySelector(".abs-shortcut-badge")) return;
    el.classList.add("abs-highlight");
    const badge = document.createElement("span");
    badge.className = "abs-shortcut-badge";
    badge.textContent = key;
    el.appendChild(badge);
    shortcutMap.set(key.toLowerCase(), el);
  }

  function clearAll() {
    document.querySelectorAll(".abs-shortcut-badge").forEach(b => b.remove());
    document.querySelectorAll(".abs-highlight").forEach(el => el.classList.remove("abs-highlight"));
    shortcutMap.clear();
  }

  window.addEventListener("keydown", (e) => {
    const isInput = document.activeElement.tagName.match(/INPUT|TEXTAREA/) || document.activeElement.isContentEditable;
    
    if (e.altKey && e.code === "KeyM") { // Auto-map
      e.preventDefault(); clearAll();
      const btns = Array.from(document.querySelectorAll('button, [role="button"], .btn')).filter(b => b.offsetHeight > 0);
      btns.slice(0, keys.length).forEach((b, i) => attachBadge(b, keys[i]));
    }
    else if (e.altKey && e.code === "KeyS") { // Toggle Inspect
      e.preventDefault(); inspectMode = !inspectMode;
    }
    else if (e.altKey && e.code === "KeyC") { // Clear
      clearAll();
    }
    else if (inspectMode && hovered && e.key.length === 1 && !e.ctrlKey && !e.altKey) { // Bind custom
      e.preventDefault(); attachBadge(hovered, e.key.toUpperCase()); inspectMode = false;
    }
    else if (!isInput && !e.ctrlKey && !e.altKey) { // Trigger click
      const btn = shortcutMap.get(e.key.toLowerCase());
      if (btn) { e.preventDefault(); btn.click(); }
    }
  }, true);

  window.addEventListener("mouseover", (e) => {
    if (!inspectMode) return;
    if (hovered && hovered !== e.target) hovered.classList.remove("abs-highlight");
    hovered = e.target.closest("button, a, [role='button']") || e.target;
    hovered.classList.add("abs-highlight");
  });
})();"""

# Write files
files = {
    "manifest.json": manifest_data,
    "styles.css": css_data,
    "content.js": js_data
}

for filename, content in files.items():
    with open(os.path.join(folder_name, filename), "w") as f:
        f.write(content)

print(f"Success! Extension generated in the '{folder_name}' folder.")
print("You can now load this folder as an unpacked extension in Chrome.")
