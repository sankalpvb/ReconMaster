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

// We export the function so main.js can import it.
// Note: Gobuster doesn't have a reference table, so we export a blank function for consistency.
export { createGobusterOptions, function createGobusterReferenceTable() { return ''; } };
