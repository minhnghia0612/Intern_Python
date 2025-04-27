async function button_add(operation) {
    const inputJobElement = document.getElementById('job');
    const inputDateElement = document.getElementById('date');

    const inputJob = inputJobElement.value.trim();
    const inputDate = inputDateElement.value;

    if (inputJob === '' || inputDate === '') {
        alert('An error');
        return;
    }

    try {
        const response = await fetch('/button_add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                inputJob: inputJob,
                inputDate: inputDate,
                operation: operation
            })
        });
        const data = await response.json();
        loadJob();

        inputJobElement.value='';
        inputDateElement.value='';
    } catch (error) {
        console.error('Error:', error);
        alert('An error');
    }
}

async function loadJob() {
    try {
        const response = await fetch('/task');
        const data = await response.json();
        const table = document.getElementById('task');
        table.innerHTML = '';

        data.forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.job}</td>
                <td>${item.date}</td>
                <td><button onclick="button_delete('${item.job}', '${item.date}')">X</button></td>
            `;
            table.appendChild(row);
        });
    } catch (error) {
        console.error('Error:', error);
        alert('An error');
    }
}
async function button_delete(job, date) {
    try{
        const response = await fetch('/button_delete', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                inputJob: job,
                inputDate: date,
                operation: 'delete'
            })
        })
        const data = await response.json();
        loadJob();
    }catch(error){
        console.error('Error:', error);
        alert('An error');
    }

}