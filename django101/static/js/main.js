function highlight() {
    if (this.className.includes('highlighted')) {
        this.className = this.className.replace('highlighted', '')
    } else {
        this.className += ' highlighted';
    }
}

window.onload = function () {
    [...document.getElementsByClassName('highlightable')]
        .forEach(element => {
            console.log(element)
            element.addEventListener('mouseenter', highlight);
            element.addEventListener('mouseleave', highlight);
        });
}

// $(document).ready(function () {
//     const arrow = $(".arrow-up");
//     const form = $(".login-form");
//     let status = false;
//
//     $('#Login').click(function (event) {
//         event.preventDefault();
//         if (status === false) {
//             arrow.fadeIn();
//             form.fadeIn();
//             status = true;
//         } else {
//             arrow.fadeOut();
//             form.fadeOut();
//             status = false;
//         }
//     })
// })
//
// setTimeout(function () {
//     alert('It works!')
// }, 1500)
//
