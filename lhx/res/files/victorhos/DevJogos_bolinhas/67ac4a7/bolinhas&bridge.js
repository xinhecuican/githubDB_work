
function randomNumberWithLimit(start, limit){

    var number;

    do {
        number = Math.floor(Math.random() * limit);
    }
    while ((number < start) || (number > limit))

    return number

}

//Funcao que cria as bolinhas
function createElements(qtd_elements){
    
    qtd = qtd_elements;

    for (var i = 0; i <= qtd; i++){

        list_ball['bolinha' + i] = game.add.sprite(
                                        randomNumberWithLimit(100, 600), 
                                        randomNumberWithLimit(100, 600), 
                                        'balls', 
                                        0);

    }

}

function createBridge(){

    for (i in list_ball){

        list_bridge['bridge' + i] = [];

        //limite qtd de ligações 
        var qtd_limit = qtd - 1;
        //qtd de ligações
        var qtd_bridges = Math.floor(Math.random() * qtd_limit); 

        //bolinhas ligadas
        for (var j = 0; j < qtd_bridges; j++){

            var number;


            do {
                number = Math.floor(Math.random() * limit);
            }
            while (number == i)
                
            list_bridge['bridge' + i].push(number);

        }

    }

}



























