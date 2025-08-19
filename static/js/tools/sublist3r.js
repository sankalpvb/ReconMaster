// reconmaster/static/js/tools/sublist3r.js

function createOptionsUI() {
    return `
        <div class="mb-3">
            <label class="form-label">Target Domain</label>
            <input type="text" class="form-control" id="target-input" placeholder="example.com">
        </div>
        <p class="text-muted">Sublist3r does not require additional options. It will use multiple search engines to find subdomains.</p>
    `;
}

function createReferenceUI() {
    return `
        <h5>Sublist3r Quick Reference</h5>
        <table class="table table-sm mt-3">
            <thead class="table-dark"><tr><th>Flag</th><th>Description</th></tr></thead>
            <tbody>
                <tr><td>-d</td><td>Specify the domain to enumerate</td></tr>
                <tr><td>-p</td><td>Scan specific TCP ports on found subdomains</td></tr>
                <tr><td>-v</td><td>Enable verbose mode</td></tr>
                <tr><td>-t</td><td>Number of threads to use</td></tr>
                <tr><td>-e</td><td>Specify a search engine (e.g., google, yahoo)</td></tr>
            </tbody>
        </table>
    `;
}

export { createOptionsUI, createReferenceUI };
