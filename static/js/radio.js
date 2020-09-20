let textwatermark = document.querySelector('#text')
let showTextInput = document.querySelector('#in-text-water')

let uploadWatermatk = document.querySelector('#image-upload')
let upload = document.querySelector('.upload')

textwatermark.addEventListener("change", function(){
    let isChecked = textwatermark.checked

    if (isChecked == true) {
        showTextInput.style.display = "block"
        upload.style.display = "none"
    }
})

uploadWatermatk.addEventListener("change", function(){
    let isChecked2 = uploadWatermatk.checked

    if (isChecked2 == true) {

        upload.style.display = "block"
        showTextInput.style.display = "none"
    }
})


    

