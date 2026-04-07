const posizione_iniziale_talpa = 120;
let posizione_talpa = posizione_iniziale_talpa;

const talpa_step = 2;
const intervallo_step = 1;
let talpa_partita_epoch;
let timeout_talpa;

function start_game() {
    reset_game();
    const start_button = document.querySelector(".start");
    start_button.style = "display: none";
    const minimo = 3000;
    const massimo = 15000;
    const casuale = Math.random();
    const timeout = casuale * (massimo - minimo) + minimo;
    console.log("timeout:", timeout);
    posizione_talpa = posizione_iniziale_talpa;
    timeout_talpa = setTimeout(talpa_GO, timeout);
}

function talpa_GO() {
    console.log("inizio talpa_GO");

    talpa_partita_epoch = new Date().getTime();

    timeout_talpa = setTimeout(sposta_talpa, intervallo_step);
}

function sposta_talpa() {
    posiziona_talpa(posizione_talpa - talpa_step);
    // console.log("posizione:", posizione_talpa);
    // console.log("style:", immagine_talpa.style);
    if(posizione_talpa > 0) {
        timeout_talpa = setTimeout(sposta_talpa, intervallo_step);
    }
}

function posiziona_talpa(nuova_posizione) {
    const immagine_talpa = document.getElementById("talpa");
    const immagine_talpa_colpita = document.getElementById("talpa_colpita");
    posizione_talpa = nuova_posizione;
    immagine_talpa.style.top = posizione_talpa + "px";
    immagine_talpa_colpita.style.top = posizione_talpa + "px";
}

function reset_game() {
    posiziona_talpa(posizione_iniziale_talpa);
    const immagine_talpa_colpita = document.getElementById("talpa_colpita");
    immagine_talpa_colpita.style = "display: none";
}
function talpa_colpita() {
    clearTimeout(timeout_talpa);
    const lista_risultati = document.getElementById("risultati");
    if(posizione_talpa === posizione_iniziale_talpa){
        console.log("Schiacciato prima della partenza");
        lista_risultati.innerHTML = lista_risultati.innerHTML + "<li>Hai barato</li>";
    } else {
        console.log("talpa colpita");
        const img_talpa_colpita = document.getElementById("talpa_colpita");
        img_talpa_colpita.style = "display: block";
        const talpa_colpita_epoch = new Date().getTime();
        const tempo_passato = talpa_colpita_epoch - talpa_partita_epoch;
        console.log("tempo passato", tempo_passato);
        lista_risultati.innerHTML = lista_risultati.innerHTML + "<li>" + tempo_passato / 1000 + "</li>";
    }
    const start_button = document.querySelector(".start");
    start_button.style = "display: block";
}