uploadForm.addEventListener('submit', (e) => {
  e.preventDefault();
  uploadStatus.classList.add('hidden');
  uploadError.classList.add('hidden');

  const fileInput = uploadForm['resume-file'];
  const file = fileInput.files[0];
  if (!file) {
    uploadError.textContent = 'Please select a resume file to upload.';
    uploadError.classList.remove('hidden');
    return;
  }

  const formData = new FormData();
  formData.append('resume', file);

  uploadStatus.textContent = 'Parsing resume...';
  uploadStatus.classList.remove('hidden');

  fetch('http://localhost:5000/upload', {
    method: 'POST',
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      uploadStatus.textContent = Resume '${file.name}' parsed successfully.;

      // Aapke dashboard ya parsed list me yeh data add kare
      console.log('Parsed Data:', data);
      // Yahan code likh sakte ho to update frontend dynamically

    })
    .catch(err => {
      console.error(err);
      uploadError.textContent = 'Failed to parse resume.';
      uploadError.classList.remove('hidden');
    });
});
