function funkcja_zwrotna() {
    var poleTekstowe = document.getElementById('pole_tekstowe').value;
    var poleLiczbowe = document.getElementById('pole_liczbowe').value;

    console.log(`${poleTekstowe}:${typeof poleTekstowe}`);
    console.log(`${poleLiczbowe}:${typeof poleLiczbowe}`);
  }