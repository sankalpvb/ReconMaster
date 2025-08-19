// reconmaster/static/js/tools/assetfinder.js

function createOptionsUI() {
    return `
        <div class="mb-3">
            <label class="form-label">Target Domain</label>
            <input type="text" class="form-control" id="target-input" placeholder="example.com">
        </div>
        <p class="text-muted">Assetfinder does not require additional options for a standard subdomain scan.</p>
    `;
}

function createReferenceUI() {
    return `
        <h5>Assetfinder Quick Reference</h5>
        <table class="table table-sm mt-3">
            <thead class="table-dark"><tr><th>Flag</th><th>Description</th></tr></thead>
            <tbody>
                <tr><td>--subs-only</td><td>Only output subdomains for the given domain</td></tr>
            </tbody>
        </table>
    `;
}

export { createOptionsUI, createReferenceUI };
