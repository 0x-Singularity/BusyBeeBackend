const backendURL = 'http:localhost:5000';

document.querySelector('form').addEventListener('submit', async function(event) {
  event.preventDefault();
  const.formData = new FormData(this);
  const response = await fetch(backenURL + '/predict_image', {
    method: 'POST',
    body: FormData
  });

  const result = await response.json();
  document.getElementByID('prediction_result').innerText = result.prediction;
});
