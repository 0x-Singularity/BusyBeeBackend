document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData();
    formData.append('file', document.getElementById('file-input').files[0]);
    const response = await fetch('/predict_image', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    const predictionResult = document.getElementById('prediction_result');
    predictionResult.innerHTML = ''; // Clear previous results
    const resultHeading = document.createElement('h2');
    resultHeading.textContent = 'Prediction Results:';
    predictionResult.appendChild(resultHeading);
    const resultList = document.createElement('ul');
    result.predictions.forEach(function(prediction) {
        const label = prediction[0];
        const score = prediction[1];
        const listItem = document.createElement('li');
        listItem.textContent = `${label}: ${score}`;
        resultList.appendChild(listItem);
    });
    predictionResult.appendChild(resultList);
});
