
let choice = document.querySelector('.choice')

let video = document.querySelector('.video')
let image = document.querySelector('.image')

let apply = document.querySelector('.apply')

video.addEventListener("click", function(){
    choice.innerHTML = "video"
    apply.style.display = "block"
})

image.addEventListener("click", function(){
    choice.innerHTML = "image"
    apply.style.display = "block"
})






