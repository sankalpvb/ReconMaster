// reconmaster/static/js/history.js

document.addEventListener('DOMContentLoaded', function() {
    const historyContainer = document.getElementById('history-container');

    async function fetchAndDisplayHistory() {
        historyContainer.innerHTML = '<p>Loading history...</p>';
        try {
            const response = await fetch('/api/scans');
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            
            const scans = await response.json();
            
            if (scans.length === 0) {
                historyContainer.innerHTML = '<div class="alert alert-info">No saved scans found.</div>';
                return;
            }

            let historyHtml = '<div class="accordion" id="historyAccordion">';
            scans.forEach((scan, index) => {
                const scanDate = new Date(scan.timestamp).toLocaleString();
                historyHtml += `
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="heading${index}">
                            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${index}">
                                <strong>${scan.tool.name}</strong> on <strong>${scan.target}</strong> - <span class="text-muted ms-2">${scanDate}</span>
                            </button>
                        </h2>
                        <div id="collapse${index}" class="accordion-collapse collapse" data-bs-parent="#historyAccordion">
                            <div class="accordion-body">
                                <p><strong>Options:</strong> <code>${scan.options || 'None'}</code></p>
                                <pre id="history-output-area">${scan.output}</pre>
                            </div>
                        </div>
                    </div>
                `;
            });
            historyHtml += '</div>';
            historyContainer.innerHTML = historyHtml;

        } catch (error) {
            historyContainer.innerHTML = '<div class="alert alert-danger">Failed to load scan history.</div>';
            console.error("History fetch error:", error);
        }
    }

    // Load history when the page loads
    fetchAndDisplayHistory();
});
