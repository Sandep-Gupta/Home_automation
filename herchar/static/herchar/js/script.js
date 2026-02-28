const apiUrl = '/api/appliances/';

// Get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Load appliances from API
function loadAppliances() {
    fetch(apiUrl)
        .then(res => res.json())
        .then(data => {
            const container = document.getElementById('appliances');
            container.innerHTML = '';

            data.forEach(device => {

                const card = document.createElement('div');
                card.className = 'appliance';

                const statusClass = device.status ? 'status-on' : 'status-off';
                const buttonClass = device.status ? 'on' : 'off';
                const statusText = device.status ? 'ON' : 'OFF';
                const buttonText = device.status ? 'Turn OFF' : 'Turn ON';

                card.innerHTML = `
                    <h3>${device.name}</h3>
                    <p>Status: <strong class="${statusClass}">${statusText}</strong></p>
                    <button class="${buttonClass}" onclick="toggleDevice(${device.id})">
                        ${buttonText}
                    </button>
                `;

                container.appendChild(card);
            });
        });
}

// Toggle appliance
function toggleDevice(id) {
    fetch(`/api/toggle/${id}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({})
    })
    .then(() => loadAppliances());
}

// Load devices when page loads
document.addEventListener("DOMContentLoaded", function() {
    loadAppliances();
});