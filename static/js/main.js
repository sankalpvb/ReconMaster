// reconmaster/static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    const toolList = document.getElementById('tool-list');
    const mainContent = document.getElementById('main-content');
    const referenceColumn = document.getElementById('reference-column');
    const suggestionModal = new bootstrap.Modal(document.getElementById('suggestionModal'));
    const suggestionModalBody = document.getElementById('suggestionModalBody');
    let socket = null;
    let currentScanData = {};

    // --- Tool Fetching and Displaying ---
    async function fetchTools() {
        try {
            const response = await fetch('/api/tools');
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const tools = await response.json();
            displayTools(tools);
        } catch (error) { console.error("Failed to fetch tools:", error); }
    }

    function displayTools(tools) {
        toolList.innerHTML = '';
        tools.forEach(tool => {
            const toolElement = document.createElement('a');
            toolElement.href = '#';
            toolElement.className = 'list-group-item list-group-item-action';
            toolElement.textContent = tool.name;
            toolElement.dataset.toolId = tool.id;
            toolList.appendChild(toolElement);
        });
    }

    async function fetchAndDisplayToolDetails(toolId) {
        try {
            const response = await fetch(`/api/tools/${toolId}`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const tool = await response.json();
            updateMainContent(tool);
        } catch (error) { console.error("Failed to fetch tool details:", error); }
    }

    // --- Main Content Update ---
    async function updateMainContent(tool) {
        let optionsHtml = '';
        referenceColumn.innerHTML = '';
        try {
            const toolModuleName = tool.name.toLowerCase();
            const toolModule = await import(`./tools/${toolModuleName}.js`);
            
            if (toolModule.createGobusterOptions && toolModuleName === 'gobuster') {
                 optionsHtml = toolModule.createGobusterOptions();
            } else if (toolModule.createNmapOptions) {
                 optionsHtml = toolModule.createNmapOptions();
            }

            if (toolModule.createNmapReferenceTable) {
                referenceColumn.innerHTML = toolModule.createNmapReferenceTable();
            } else if (toolModule.createGobusterReferenceTable) {
                referenceColumn.innerHTML = toolModule.createGobusterReferenceTable();
            }

        } catch (error) {
            console.warn(`No specific UI module found for ${tool.name}.`, error);
        }
        mainContent.innerHTML = `<h2 class="card-title">${tool.name} <span class="badge bg-secondary">${tool.category}</span></h2><p class="card-text">${tool.description}</p><h5>Advantages</h5><p>${tool.advantages}</p><h5>Example Usage</h5><pre><code>${tool.example_usage}</code></pre><hr><div id="parsed-results-container" class="mb-4"></div><h4>Run Tool</h4><div class="mb-3"><label for="target-input" class="form-label">Target</label><input type="text" class="form-control" id="target-input" placeholder="example.com"></div>${optionsHtml}<div id="action-buttons" class="mt-4"><button class="btn btn-primary" id="run-tool-btn" data-tool-id="${tool.id}" data-tool-name="${tool.name}">Run Scan</button><button class="btn btn-danger" id="cancel-tool-btn" style="display: none;">Cancel Scan</button></div><h4 class="mt-4">Raw Output</h4><div id="output-area"></div>`;
    }

    // --- Function to display parsed results ---
    function displayParsedResults(toolName, parsedData) {
        const container = document.getElementById('parsed-results-container');
        if (!container) return;

        let tableHtml = '';
        if (toolName === 'Nmap') {
            tableHtml = `<h4>Analysis & Next Steps</h4><div class="table-responsive"><table class="table table-striped table-bordered"><thead class="table-dark"><tr><th>Port</th><th>State</th><th>Service</th><th>Suggested Next Step</th></tr></thead><tbody>`;
            parsedData.forEach(port => {
                tableHtml += `<tr><td>${port.port}</td><td><span class="badge bg-success">${port.state}</span></td><td>${port.service}</td><td>${port.suggestion}</td></tr>`;
            });
            tableHtml += '</tbody></table></div>';
        } else if (toolName === 'Gobuster') {
            tableHtml = `<h4>Analysis: Found Paths</h4><div class="table-responsive"><table class="table table-striped table-bordered"><thead class="table-dark"><tr><th>Path</th><th>Status</th><th>Size (Bytes)</th><th>Suggestion</th></tr></thead><tbody>`;
            parsedData.forEach(path => {
                tableHtml += `<tr><td>${path.path}</td><td><span class="badge bg-info">${path.status}</span></td><td>${path.size}</td><td><button class="btn btn-sm btn-outline-info suggestion-btn" data-suggestion="${path.suggestion}"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-info-circle" viewBox="0 0 16 16" style="pointer-events: none;"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="m8.93 6.588-2.29.287-.082.38.45.083c.294.055.491.223.57.45.079.227.028.473-.143.645-.17.172-.396.256-.643.256h-.102c-.247 0-.473-.084-.643-.256-.172-.172-.223-.418-.143-.645.079-.227.276-.395.57-.45l.45-.083-.082-.38-2.29-.287A1.76 1.76 0 0 0 4 8.25c0 .966.784 1.75 1.75 1.75A1.76 1.76 0 0 0 7.5 8.25c0-.966-.784-1.75-1.75-1.75zM8 4a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/></svg></button></td></tr>`;
            });
            tableHtml += '</tbody></table></div>';
        }
        container.innerHTML = tableHtml;
    }
    
    // --- Save Scan Function ---
    async function saveCurrentScan() {
        if (!currentScanData.output) { alert("No scan output to save."); return; }
        try {
            const response = await fetch('/api/scans', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(currentScanData),
            });
            if (!response.ok) throw new Error('Failed to save scan.');
            const saveBtn = document.getElementById('save-scan-btn');
            saveBtn.textContent = 'Saved!';
            saveBtn.classList.replace('btn-success', 'btn-secondary');
            saveBtn.disabled = true;
        } catch (error) { console.error("Save scan error:", error); alert("Error saving scan."); }
    }

    // --- Event Listeners ---
    mainContent.addEventListener('input', function(event) {
        const toolName = document.getElementById('run-tool-btn')?.dataset.toolName;
        if (toolName === 'Nmap' && (event.target.id === 'nmap-flags-input' || event.target.id === 'target-input')) {
            const flags = document.getElementById('nmap-flags-input').value;
            const targetVal = document.getElementById('target-input').value || '<target>';
            document.getElementById('command-preview').textContent = `nmap ${flags} ${targetVal}`;
        }
    });

    mainContent.addEventListener('click', function(event) {
        const suggestionBtn = event.target.closest('.suggestion-btn');
        if (suggestionBtn) {
            const suggestionText = suggestionBtn.dataset.suggestion;
            suggestionModalBody.textContent = suggestionText;
            suggestionModal.show();
            return;
        }
        
        const targetEl = event.target;
        if (targetEl && targetEl.id === 'run-tool-btn') {
            const toolId = targetEl.dataset.toolId;
            const toolName = targetEl.dataset.toolName;
            const targetInput = document.getElementById('target-input');
            const targetValue = targetInput.value.trim();
            const outputArea = document.getElementById('output-area');
            let optionsValue = '';
            if (toolName === 'Nmap') optionsValue = document.getElementById('nmap-flags-input').value;
            else if (toolName === 'Gobuster') optionsValue = document.querySelector('input[name="scan-options"]:checked')?.value || '';
            if (!targetValue) { outputArea.textContent = 'ERROR: Please enter a target.'; return; }
            if (socket) { socket.close(); }
            currentScanData = { tool_id: toolId, target: targetValue, options: optionsValue, output: '' };
            startWebSocket(toolId, targetValue, optionsValue, outputArea);
        }
        if (targetEl && targetEl.id === 'cancel-tool-btn') { if (socket) { socket.close(); } }
        if (targetEl && targetEl.id === 'save-scan-btn') { saveCurrentScan(); }
    });

    // --- WebSocket Logic ---
    function startWebSocket(toolId, target, options, outputArea) {
        const runBtn = document.getElementById('run-tool-btn');
        const cancelBtn = document.getElementById('cancel-tool-btn');
        const actionButtons = document.getElementById('action-buttons');
        const parsedContainer = document.getElementById('parsed-results-container');
        document.getElementById('save-scan-btn')?.remove();
        if(parsedContainer) parsedContainer.innerHTML = '';
        runBtn.style.display = 'none';
        cancelBtn.style.display = 'inline-block';
        outputArea.innerHTML = '<p class="text-info">Connecting to server...</p>';
        const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const wsUrl = `${wsProtocol}//${window.location.host}/api/ws/run/${toolId}`;
        socket = new WebSocket(wsUrl);
        socket.onopen = function() {
            outputArea.innerHTML = '<p class="text-success">Connection successful! Sending command...</p>';
            const payload = JSON.stringify({ target: target, options: options });
            socket.send(payload);
        };
        socket.onmessage = function(event) {
            try {
                const parsedMessage = JSON.parse(event.data);
                if (parsedMessage.type === 'parsed_data') {
                    displayParsedResults(parsedMessage.tool, parsedMessage.data);
                    return;
                }
            } catch (e) { /* Not JSON, treat as raw output */ }
            if (!event.data.startsWith("INFO:") && !event.data.startsWith("ERROR:")) {
                currentScanData.output += event.data + '\n';
            }
            const message = document.createElement('div');
            message.textContent = event.data;
            outputArea.appendChild(message);
            outputArea.scrollTop = outputArea.scrollHeight;
        };
        socket.onclose = function() {
            const message = document.createElement('p');
            message.className = 'text-warning mt-2';
            message.textContent = 'Connection closed.';
            outputArea.appendChild(message);
            runBtn.style.display = 'inline-block';
            cancelBtn.style.display = 'none';
            if (currentScanData.output) {
                const saveBtn = document.createElement('button');
                saveBtn.id = 'save-scan-btn';
                saveBtn.className = 'btn btn-success ms-2';
                saveBtn.textContent = 'Save Results';
                actionButtons.appendChild(saveBtn);
            }
        };
        socket.onerror = function() {
            const message = document.createElement('p');
            message.className = 'text-danger mt-2';
            message.textContent = 'An error occurred.';
            outputArea.appendChild(message);
            runBtn.style.display = 'inline-block';
            cancelBtn.style.display = 'none';
        };
    }
    
    toolList.addEventListener('click', function(event) {
        if (event.target && event.target.matches('a.list-group-item-action')) {
            event.preventDefault();
            const toolId = event.target.dataset.toolId; 
            if (toolId) { fetchAndDisplayToolDetails(toolId); }
        }
    });

    fetchTools();
});
