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

if (navToggleBtn[0]){
    navToggleBtn[0].addEventListener('click', toggleNav)

}

// codemirror

let codeEditorMirrorDiv= document.querySelector('#editor');

let myCodeMirror = CodeMirror(codeEditorMirrorDiv, {
  value: "function myScript(){return 100;}\n",
  mode:  "javascript",
  lineNumbers: true,
  
});

