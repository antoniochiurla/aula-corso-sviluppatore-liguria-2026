let posizione_talpa = 120;
const talpa_step = 1;
const intervallo_step = 10;
let talpa_partita_epoch;

function start_game() {
    const start_button = document.querySelector(".start");
    start_button.style = "display: none";
    const minimo = 500; // 3000;
    const massimo = 1000; // 15000;
    const casuale = Math.random();
    const timeout = casuale * (massimo - minimo) + minimo;
    console.log("timeout:", timeout);
    setTimeout(talpa_GO, timeout);
}

function talpa_GO() {
    console.log("inizio talpa_GO");

    talpa_partita_epoch = new Date().getTime();

    setTimeout(sposta_talpa, intervallo_step);
}

function sposta_talpa() {
    const immagine_talpa = document.getElementById("talpa");
    posizione_talpa = posizione_talpa - talpa_step;
    immagine_talpa.style.top = posizione_talpa + "px";
    // console.log("posizione:", posizione_talpa);
    // console.log("style:", immagine_talpa.style);
    if(posizione_talpa > 0) {
        setTimeout(sposta_talpa, intervallo_step);
    }
}

function talpa_colpita() {
    console.log("talpa colpita");
    const talpa_colpita_epoch = new Date().getTime();
    const tempo_passato = talpa_colpita_epoch - talpa_partita_epoch;
    console.log("tempo passato", tempo_passato);
}