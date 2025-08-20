    // reconmaster/static/js/tools/ffuf.js
    function createOptionsUI() {
        return `
            <div class="mb-3">
                <label class="form-label">Target URL (use 'FUZZ' keyword)</label>
                <input type="text" class="form-control" id="target-input" placeholder="http://example.com/FUZZ">
            </div>
            <h6>Wordlist</h6>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="scan-options" value="/usr/share/wordlists/dirb/common.txt" checked>
                <label class="form-check-label" for="opt-common">Common Directories</label>
            </div>
        `;
    }
    function createReferenceUI() { /* ... content ... */ }
    export { createOptionsUI, createReferenceUI };
    
