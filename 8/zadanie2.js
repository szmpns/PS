function sum(x,y) {
    return x+y;
}

function sum_strings(a) {
    let sum = 0

    for(let str of a){
        const cyfra = str.match(/^\d+/);

        if(cyfra){
            const liczba = parseInt(cyfra[0]); 
            sum += liczba;
        }
    }

    return sum
}


function digits(s) {
    let suma_liczb_nieparzystych = 0
    let suma_liczb_parzystych = 0

    for(let i = 0 ; i < s.length ; i ++ ){
        const liczba = parseInt(s[i])

        if(!isNaN(liczba)){
            if(liczba % 2 == 0){
                suma_liczb_parzystych += liczba
            }
            else{
                suma_liczb_nieparzystych += liczba
            }
        }
    }

    return [suma_liczb_nieparzystych , suma_liczb_parzystych]
}

function letters(s) {
    let ilość_małych_liter = 0
    let ilość_dużych_liter = 0

    for(let i = 0 ; i < s.length ; i++){
        const litera = s[i]

        if(/[a-z]/.test(litera)){
            ilość_małych_liter++
        }
        else if(/[A-Z]/.test(litera)) {
            ilość_dużych_liter++
        }
    }

    return [ilość_małych_liter , ilość_dużych_liter]
}