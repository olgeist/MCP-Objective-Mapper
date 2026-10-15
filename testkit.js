class AutoButtonTestkit {
    constructor(logContainerId) {
        this.logContainer = document.getElementById(logContainerId);
        this.init();
    }

    init() {
        this.setupExtensionListener();
        this.attachClickMonitors();
        this.log("Testkit initialized. Waiting for extension handshake...");
    }

    log(message) {
        if (!this.logContainer) return;
        const time = new Date().toLocaleTimeString();
        const entry = document.createElement('div');
        entry.textContent = `[${time}] ${message}`;
        this.logContainer.prepend(entry);
    }

    setupExtensionListener() {
        document.addEventListener('AutoButtonExtensionActive', (e) => {
            this.log(`✅ Extension Detected: Version ${e.detail.version}`);
            document.body.classList.add('extension-active');
        });

        setTimeout(() => {
            if (!document.body.classList.contains('extension-active')) {
                this.log("⚠️ Extension not detected. Is it installed and enabled?");
            }
        }, 1500);
    }

    attachClickMonitors() {
        const clickableElements = document.querySelectorAll('button, .btn, input[type="button"], input[type="submit"], [role="button"]');
        
        clickableElements.forEach(el => {
            el.addEventListener('click', (e) => {
                e.preventDefault(); 
                const name = el.getAttribute('data-test-name') || el.innerText || el.value || 'Unknown Button';
                this.log(`CLICK DETECTED: ${name}`);
                
                // Visual flash
                const originalBg = el.style.backgroundColor;
                el.style.backgroundColor = '#ffffff';
                setTimeout(() => el.style.backgroundColor = originalBg, 150);
            });
        });
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.testkit = new AutoButtonTestkit('console-log');
});
