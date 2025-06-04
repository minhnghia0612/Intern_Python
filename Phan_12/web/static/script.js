document.getElementById('predictionForm').addEventListener('submit', async(e) => {
    e.preventDefault(); //Ngăn trang load lại

    const area = parseFloat(document.getElementById('area').value);
    const bedrooms = parseInt(document.getElementById('bedrooms').value);
    const bathrooms = parseInt(document.getElementById('bathrooms').value);
    const stories = parseInt(document.getElementById('stories').value);


    try{
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                area: area, 
                bedrooms: bedrooms,
                bathrooms: bathrooms,
                stories: stories
            })
        });

        if (response.ok) {
            const result = await response.json();
            const formattedPrice = Math.round(result.predicted_price).toLocaleString('vi-VN') + ' VNĐ';
            document.getElementById('resultMessage').innerText = `Giá dự đoán: ${formattedPrice}`;
        }
        else{
            const errorData = await response.json();
            document.getElementById('resultMessage').textContent = errorData.error || 'Đã xảy ra lỗi khi dự đoán giá nhà.';
        }
    } catch (error) {
        console.error('Lỗi khi gửi yêu cầu:', error);
        document.getElementById('resultMessage').textContent = 'Đã xảy ra lỗi khi gửi yêu cầu: ' + error.message;
    }
});
