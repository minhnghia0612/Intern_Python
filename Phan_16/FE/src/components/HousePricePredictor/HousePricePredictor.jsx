import { useState } from 'react';
import './HousePricePredictor.css';

function HousePricePredictor() {
  const [area, setArea] = useState('');
  const [bedrooms, setBedrooms] = useState('');
  const [bathrooms, setBathrooms] = useState('');
  const [stories, setStories] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/predict-house', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          area: Number(area),
          bedrooms: Number(bedrooms),
          bathrooms: Number(bathrooms),
          stories: Number(stories)
        })
      });

      const data = await response.json();
      setResult(`Dự đoán giá: ${data.predicted_price.toLocaleString()} VND`);
    } catch (error) {
      console.error('Prediction error:', error);
      setResult('Có lỗi xảy ra khi dự đoán.');
    }
  };

  return (
    <div className="predictor-container">
      <h1 className="predictor-title">House price prediction</h1>
      <form className="predictor-form" onSubmit={handleSubmit}>
        <input
          type="number"
          className="predictor-input"
          placeholder="Nhập diện tích mảnh đất"
          value={area}
          onChange={(e) => setArea(e.target.value)}
          required
        />
        <input
          type="number"
          className="predictor-input"
          placeholder="Nhập số phòng ngủ"
          value={bedrooms}
          onChange={(e) => setBedrooms(e.target.value)}
          required
        />
        <input
          type="number"
          className="predictor-input"
          placeholder="Nhập số phòng tắm"
          value={bathrooms}
          onChange={(e) => setBathrooms(e.target.value)}
          required
        />
        <input
          type="number"
          className="predictor-input"
          placeholder="Nhập số tầng"
          value={stories}
          onChange={(e) => setStories(e.target.value)}
          required
        />
        <button type="submit" className="predictor-button">
          Predict Price
        </button>
      </form>
      <div className="predictor-result">{result}</div>
    </div>
  );
}

export default HousePricePredictor;
