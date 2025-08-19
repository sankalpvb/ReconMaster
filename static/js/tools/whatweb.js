// reconmaster/static/js/tools/whatweb.js

function createOptionsUI() {
    return `
        <div class="mb-3">
            <label class="form-label">Target URL or Host</label>
            <input type="text" class="form-control" id="target-input" placeholder="http://example.com">
        </div>
        <p class="text-muted">WhatWeb does not require additional options for a standard scan.</p>
    `;
}

function createReferenceUI() {
    return `
        <h5>WhatWeb Quick Reference</h5>
        <table class="table table-sm mt-3">
            <thead class="table-dark"><tr><th>Flag</th><th>Description</th></tr></thead>
            <tbody>
                <tr><td>-a</td><td>Set aggression level (1-4)</td></tr>
                <tr><td>-v</td><td>Enable verbose output</td></tr>
                <tr><td>--no-redirect</td><td>Do not follow redirects</td></tr>
                <tr><td>-p</td><td>Specify a plugin to run</td></tr>
                <tr><td>--list-plugins</td><td>List all available plugins</td></tr>
            </tbody>
        </table>
    `;
}

export { createOptionsUI, createReferenceUI };
