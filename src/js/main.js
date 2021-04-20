

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

if (navToggleBtn[0]) {
    navToggleBtn[0].addEventListener('click', toggleNav)

}

// codemirror

let myEditorJs = document.querySelector('#editor');

let myCodeMirror = CodeMirror(myEditorJs, {
    value: "function myScript(){return 100;}\n",
    mode: "javascript",
    lineNumbers: true,

});





// Handle save response

let saveProgrammeResponseBtn = document.querySelector("#save-programming-response-button");

if (saveProgrammeResponseBtn) {
    saveProgrammeResponseBtn.addEventListener("click", saveProgrammeResponse);

    function saveProgrammeResponse() {
        let programmeResponseValue = myCodeMirror.getValue();

        // get meta data about questions and users
        let currentUser = document.querySelector("#username");
        let currentExamId = document.querySelector("#exam_id");
        let currentQuestionId = document.querySelector("#question_id");

        currentUser = currentUser.innerHTML;
        currentExamId = currentExamId.innerHTML;
        currentQuestionId = currentQuestionId.innerHTML;

        let url = "/exam/response/";

        axios({
            method: 'post',
            url: url,
            data: {
                username: currentUser,
                examId: currentExamId,
                questionId:currentQuestionId,
                editorContent:programmeResponseValue,
            }
        });


    }


}


// timer for exam

function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + " min : " + seconds + " sec";

        if (--timer < 0) {
            timer = duration;
        }
    }, 1000);
}

window.onload = function () {
    var fiveMinutes = 60 * 12,
        display = document.querySelector('#time');
    startTimer(fiveMinutes, display);
};


// testing zone



