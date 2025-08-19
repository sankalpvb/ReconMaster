// reconmaster/static/js/tools/gobuster.js

function createOptionsUI() {
    return `
        <div class="mb-3">
            <label class="form-label">Target URL</label>
            <input type="text" class="form-control" id="target-input" placeholder="http://testphp.vulnweb.com">
        </div>
        <h6>Wordlist</h6>
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

function createReferenceUI() {
    return `
        <h5>Gobuster Quick Reference</h5>
        <table class="table table-sm mt-3">
            <thead class="table-dark"><tr><th>Flag</th><th>Description</th></tr></thead>
            <tbody>
                <tr><td>dir</td><td>Directory/File brute-forcing mode</td></tr>
                <tr><td>-u</td><td>Target URL or Domain</td></tr>
                <tr><td>-w</td><td>Path to the wordlist</td></tr>
                <tr><td>-t</td><td>Number of concurrent threads</td></tr>
                <tr><td>-x</td><td>File extensions to search for</td></tr>
                <tr><td>-z</td><td>Show content size in output</td></tr>
                <tr><td>-k</td><td>Skip SSL certificate verification</td></tr>
            </tbody>
        </table>
    `;
}

export { createOptionsUI, createReferenceUI };
