var elem = document.documentElement;

let fullScreenToggleBtn = document.querySelector("#fullScreen");
let fullScreenStatus = 0;
if (fullScreenToggleBtn) {

    if (!fullScreenStatus) {
        fullScreenToggleBtn.addEventListener("click", openFullscreen);
        fullScreenStatus = 1;
    }

    fullScreenToggleBtn.addEventListener("click", openFullscreen);
    fullScreenStatus = 0;

}

/* View in fullscreen */
function openFullscreen() {
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
        elem.msRequestFullscreen();
    }
}


function closeFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.webkitExitFullscreen) { /* Safari */
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { /* IE11 */
        document.msExitFullscreen();
    }
}