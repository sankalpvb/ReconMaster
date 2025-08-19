// reconmaster/static/js/tools/nmap.js

function createOptionsUI() {
    return `
        <div class="row">
            <div class="col-md-6 mb-3">
                <label class="form-label">Target Host</label>
                <input type="text" class="form-control" id="target-input" placeholder="scanme.nmap.org">
            </div>
            <div class="col-md-6 mb-3">
                <label class="form-label">Nmap Flags</label>
                <input type="text" class="form-control" id="nmap-flags-input" placeholder="-sV -T4">
            </div>
        </div>
        <div>
            <strong>Command Preview:</strong>
            <pre class="mt-2"><code id="command-preview" class="text-muted">nmap -sV -T4 <target></code></pre>
        </div>
    `;
}

function createReferenceUI() {
    return `
        <h5>Nmap Quick Reference</h5>
        <table class="table table-sm mt-3">
            <thead class="table-dark"><tr><th>Flag</th><th>Description</th></tr></thead>
            <tbody>
               <tr><td>-sS</td><td>TCP SYN (Stealth) Scan</td></tr>
                            <tr><td>-sT</td><td>TCP Connect Scan</td></tr>
                            <tr><td>-sU</td><td>UDP Scan</td></tr>
                            <tr><td>-sV</td><td>Version Detection</td></tr>
                            <tr><td>-O</td><td>OS Detection</td></tr>
                            <tr><td>-A</td><td>Aggressive Scan (All)</td></tr>
                            <tr><td>-p-</td><td>Scan all 65535 ports</td></tr>
                            <tr><td>-F</td><td>Fast Mode (Top 100 ports)</td></tr>
                            <tr><td>-T4</td><td>Aggressive Timing</td></tr>
                            <tr><td>-sn</td><td>Ping Scan (No Ports)</td></tr>
                            <tr><td colspan="2" class="table-secondary text-center"><strong>Common Scripts</strong></td></tr>
                            <tr><td>-sC</td><td>Run default safe scripts</td></tr>
                            <tr><td>--script=vuln</td><td>Check for common vulnerabilities</td></tr>
                            <tr><td>--script=http-title</td><td>Get titles from web pages</td></tr>
                            <tr><td>--script=smb-os-discovery</td><td>Discover OS on SMB servers</td></tr>
                            <tr><td>--script=dns-brute</td><td>Brute force DNS hostnames</td></tr>
                            <tr><td>--script=vulners</td><td>Check against Vulners database</td></tr>
            </tbody>
        </table>
    `;
}

export { createOptionsUI, createReferenceUI };
