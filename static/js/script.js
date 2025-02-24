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

/* gerar codigo */
function gerarCodigo() {
    let caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890";
    let codigo = "";
    for (let i = 0; i < 6; i++) { 
        let randomIndex = Math.floor(Math.random() * caracteres.length);
        codigo += caracteres[randomIndex];
    }
    document.getElementById("cod_turma").value = codigo;
}

/* flash messages */
    setTimeout(function() {
        let flashMessage = document.getElementById("flash-message");
        if (flashMessage) {
            flashMessage.style.transition = "opacity 0.5s ease";
            flashMessage.style.opacity = "0"; 
            setTimeout(() => flashMessage.remove(), 500); // Remove o elemento após a animação
        }
    }, 3000);
