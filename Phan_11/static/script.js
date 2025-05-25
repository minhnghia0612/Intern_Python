let token = localStorage.getItem('token');

async function fetchWithAuth(url, options = {}) {
    if (!token) {
        window.location.href = '/login';
        return;
    }
    
    const headers = {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
        ...options.headers
    };

    const response = await fetch(url, { ...options, headers });
    if (response.status === 401) {
        localStorage.removeItem('token');
        window.location.href = '/login';
        return;
    }
    return response;
}

document.getElementById('form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const job = document.getElementById('job').value.trim();
    const date = document.getElementById('date').value;

    try {
        const response = await fetchWithAuth('/api/items/', {
            method: 'POST',
            body: JSON.stringify({
                job: job,
                date: date
            })
        });

        if (response.ok) {
            const item = await response.json();
            addItemToList(item);
            document.getElementById('form').reset();
        } else {
            const error = await response.json();
            alert(error.detail || 'Failed to create item');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while creating the item');
    }
});

function addItemToList(item) {
    const itemsList = document.getElementById('itemsList');
    const itemElement = document.createElement('div');
    itemElement.className = 'item';
    itemElement.dataset.id = item.id;
    
    itemElement.innerHTML = `
        <div class="item-content">
            <h3>${item.job}</h3>
            <p>${item.date}</p>
        </div>
        <div class="item-actions">
            <button class="delete">Delete</button>
        </div>
    `;
    
    itemsList.appendChild(itemElement);
    setupItemListeners(itemElement);
}

function setupItemListeners(itemElement) {
    const id = itemElement.dataset.id;
    
    itemElement.querySelector('.delete').addEventListener('click', async () => {
        if (confirm('Are you sure you want to delete this item?')) {
            try {
                const response = await fetchWithAuth(`/api/items/${id}`, {
                    method: 'DELETE'
                });

                if (response.ok) {
                    itemElement.remove();
                } else {
                    const error = await response.json();
                    alert(error.detail || 'Failed to delete item');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while deleting the item');
            }
        }
    });
}

document.getElementById('logout').addEventListener('click', async () => {
    try {
        const response = await fetchWithAuth('/logout', {
            method: 'POST'
        });

        if (response.ok) {
            localStorage.removeItem('token');
            window.location.href = '/login';
        } else {
            const error = await response.json();
            alert(error.detail || 'Failed to logout');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while logging out');
    }
});


document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetchWithAuth('/api/items/');
        if (response.ok) {
            const items = await response.json();
            items.forEach(item => addItemToList(item));
        } else {
            const error = await response.json();
            alert(error.detail || 'Failed to load items');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while loading items');
    }
}); 