// Handeling navigation toggle

let nav = document.querySelectorAll('.navbar__nav')
let navToggleBtn = document.querySelectorAll('.navbar__toggle__button')

let toggleState = 0;

let toggleNav = function () {

    nav[0].style.display = 'block';
    toggleState++;

    if (toggleState % 2 === 0) {
        nav[0].style.display = 'none';
    }

}


navToggleBtn[0].addEventListener('click', toggleNav)