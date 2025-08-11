// reconmaster/static/js/tools/gobuster.js

// This function creates the HTML for the Gobuster options panel.
function createGobusterOptions() {
    return `
        <h5 class="mt-4">Wordlist</h5>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="scan-options" id="opt-common" value="/usr/share/wordlists/dirb/common.txt" checked>
            <label class="form-check-label" for="opt-common">Common Directories</label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="scan-options" id="opt-medium" value="/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt">
            <label class="form-check-label" for="opt-medium">Medium Wordlist</label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="scan-options" id="opt-big" value="/usr/share/wordlists/dirbuster/directory-list-2.3-big.txt">
            <label class="form-check-label" for="opt-big">Big Wordlist <span class="text-muted">(May be slow)</span></label>
        </div>
    `;
}

// NEW: This function creates the HTML for the Gobuster reference table.
function createGobusterReferenceTable() {
    return `
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">Gobuster Quick Reference</h5>
                <div class="table-responsive" style="max-height: 400px; overflow-y: auto;">
                    <table class="table table-sm table-bordered table-hover">
                        <thead class="table-dark sticky-top">
                            <tr><th>Flag</th><th>Description</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>-u</td><td>Target URL or Domain</td></tr>
                            <tr><td>-w</td><td>Path to the wordlist</td></tr>
                            <tr><td>-t</td><td>Number of concurrent threads (e.g., 50)</td></tr>
                            <tr><td>-x</td><td>File extensions to search for (e.g., php,html)</td></tr>
                            <tr><td>-s</td><td>Show positive status codes (e.g., 200,301)</td></tr>
                            <tr><td>-b</td><td>Block specific status codes (e.g., 404)</td></tr>
                            <tr><td>-k</td><td>Skip SSL certificate verification</td></tr>
                            <tr><td>-U</td><td>Username for basic authentication</td></tr>
                            <tr><td>-P</td><td>Password for basic authentication</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    `;
}

// We export the functions so main.js can import them.
export { createGobusterOptions, createGobusterReferenceTable };
