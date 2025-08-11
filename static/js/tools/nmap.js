// reconmaster/static/js/tools/nmap.js

// This function creates the HTML for the Nmap reference table.
function createNmapReferenceTable() {
    return `
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">Nmap Quick Reference</h5>
                <div class="table-responsive" style="max-height: 400px; overflow-y: auto;">
                    <table class="table table-sm table-bordered table-hover">
                        <thead class="table-dark sticky-top">
                            <tr><th>Flag / Script</th><th>Description</th></tr>
                        </thead>
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
                </div>
            </div>
        </div>
    `;
}

// This function creates the HTML for the Nmap options panel (the command builder).
function createNmapOptions() {
    return `
        <div class="mt-4">
            <h5>Nmap Options</h5>
            <label for="nmap-flags-input" class="form-label">Enter Nmap flags:</label>
            <input type="text" class="form-control" id="nmap-flags-input" placeholder="-sV -sC --script=default">
            <div class="mt-3"><strong>Command Preview:</strong><pre><code id="command-preview" class="text-muted">nmap -sV -sC --script=default &lt;target&gt;</code></pre></div>
        </div>
    `;
}

// We export the functions so main.js can import them.
export { createNmapOptions, createNmapReferenceTable };
