let addLogo = document.querySelector('.addLogo')
const submitBtn = document.getElementById('submitBtn')

addLogo.addEventListener("change",  function(e){
    //Get file       
    let file = e.target.files[0];
    console.log(file);

    //Preview
    let preview = document.getElementById("thumbnail");
    preview.file = file;
    let reader = new FileReader();

    reader.onload = (function(aImg) {
        return function(e) {
        aImg.src = e.target.result;
        };
    })(preview);
    reader.readAsDataURL(file);
})

//REDUS CODE
submitBtn.addEventListener('click', () => {
    console.log(1)
    const formData = new FormData();
    formData.append('image', document.getElementById('imageInput').files[0]);
    formData.append('text', document.getElementById('textInput').value);
    formData.append('size', 'm');
    formData.append('watermarkPosition', 'center');
    fetch('/watermark/create', {
        method: 'POST',
        body: formData
    })
        .then(res => res.json())
        .then(data => {
            window.location.href = `/static/watermarkedImages/${data.image}`
        })
})