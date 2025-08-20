// reconmaster/static/js/tools/httpx.js

function createOptionsUI() {
    return `
        <div class="mb-3">
            <label class="form-label">Target Host or URL</label>
            <input type="text" class="form-control" id="target-input" placeholder="example.com">
        </div>
        <p class="text-muted">httpx will probe the target to check for a live web server and identify its technologies.</p>
    `;
}

function createReferenceUI() {
    return `
        <h5>httpx Quick Reference</h5>
        <table class="table table-sm mt-3">
            <thead class="table-dark"><tr><th>Flag</th><th>Description</th></tr></thead>
            <tbody>
                <tr><td>-u</td><td>Specify a single target URL</td></tr>
                <tr><td>-l</td><td>Specify a file containing a list of hosts</td></tr>
                <tr><td>-sc</td><td>Show status code</td></tr>
                <tr><td>-title</td><td>Show page title</td></tr>
                <tr><td>-tech-detect</td><td>Show technologies</td></tr>
                <tr><td>-no-color</td><td>Disable colored output</td></tr>
            </tbody>
        </table>
    `;
}

export { createOptionsUI, createReferenceUI };
