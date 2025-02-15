const password = document.getElementById('password');
const icon = document.getElementById('icon');

const confirm_password = document.getElementById('confirm_password');
const icon_confirm_password = document.getElementById('icon_confirm_password');

function showHide(){
    if(password.type == 'password'){
        password.setAttribute('type','text')
        icon.classList.add('hide')
    }
    else{
        password.setAttribute('type','password')
        icon.classList.remove('hide')
    }
}

function showHide2(){
    if(confirm_password.type == 'password'){
        confirm_password.setAttribute('type','text')
        icon_confirm_password.classList.add('hide')
    }
    else{
        confirm_password.setAttribute('type','password')
        icon_confirm_password.classList.remove('hide')
    }
}



/*pop up entrar em turma*/
document.addEventListener("DOMContentLoaded", function() {
    const openModal = document.getElementById("openModal");
    const modal = document.getElementById("popap");
    const overlay = document.getElementById("overlay");
    const openModal2 = document.getElementById("participarturma")

    openModal.addEventListener("click", function() {
        modal.style.display = "block";
        overlay.style.display = "block";
    });

    openModal2.addEventListener("click", function() {
        modal.style.display = "block";
        overlay.style.display = "block";
    });

    overlay.addEventListener("click", function() {
        modal.style.display = "none";
        overlay.style.display = "none";
    });
});
