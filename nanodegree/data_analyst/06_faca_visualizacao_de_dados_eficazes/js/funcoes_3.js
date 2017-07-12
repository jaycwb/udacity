// CRÉDITOS SÃO DEVIDOS A IMPLEMENTAÇÃO DO CÓDIGO ABAIXO AS OBRAS E TUTORIAIS ABAIXO:
// # https://www.packtpub.com/web-development/learning-d3js-mapping
// # https://www.packtpub.com/web-development/d3js-cutting-edge-data-visualization
// # http://www.cartographicperspectives.org/index.php/journal/article/view/cp78-sack-et-al/1359

//global variables

var myLocale = {
  "decimal": ",",
  "thousands": ".",
  "grouping": [3],
  "currency": ["R$", ""],
  "dateTime": "%a %b %e %X %Y",
  "date": "%d/%m/%Y",
  "time": "%H:%M:%S",
  "periods": ["AM", "PM"],
  "days": ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-Feira", "Sábado"],
  "shortDays": ["Dom", "Seg", "Te", "Qa", "Qi", "Sx", "Sa"],
  "months": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
  "shortMonths": ["Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
}

var localeFormatter = d3.locale(myLocale);
var myFormatter = localeFormatter.numberFormat(",.6r"); 

var dadosGeo = void 0; // VARIÁVEL QUE ARMANEZERÁ OS DADOS GEOGRÁFICOS
var dadosOlac = void 0; // VARIÁVEL QUE ARMAZENARÁ OS DADOS DE PRODUCAO DA ANP
var totalVolume = void 0; // VARIÁVEL QUE RECEBERÁ DADOS AGREGADOS (TOTAL) DE PRODUCAO DA ANP
var totalPorCategoria = void 0; // VARIÁVEL QUE RECEBERÁ DADOS AGREGADOS POR CATEGORIA

var listaVariaveis = ["Volume Total OLAC",
                      "Ciclo Otto", 
                      "Ciclo Diesel", 
                      "Engrenagens e Sistemas Circulatórios",
                      "Isolante Tipo A",
                      "Isolante Tipo B",
                      "Óleos Lubrificantes Marítimos",
                      "Óleos Lubrificantes Ferroviários",
                      "Óleos Lubrificantes para Aviação",
                      "Motores 2 tempos",
                      "Transmissões e Sistemas Hidráulicos",
                      "Outros Óleos Lubrificantes Acabados"
                      ]; 
var variavelAlvo = listaVariaveis[0]; // VARIÁVEL SELECIONADA

//FUNCAO QUE SERÁ CARREGADA QUANDO O HTML CARREGAR
function initialize(){
    setMap();
};


//PARAMETROS DO MAPA
function setMap(){
    // DEFINIÇÃO DAS DIMENSÕES DO SVG E DA PROJEÇÃO QUE SERÁ UTILIZADA
    var height = 600;
    var width = 500;
    var projection = d3.geo.mercator();

    // Special d3 helper that converts geo coordinates to paths
    // based on a projection
    var path = d3.geo.path().projection(projection);
    var svg = d3.select("#map")
        .classed("svg-container", true)
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    //use queue.js to parallelize asynchronous data loading
    d3.queue()
        .defer(d3.csv, "./data/producao_olac_M3.csv") //load attributes from csv
        .defer(d3.json, "./data/br-states.json") //load geographic data
        .await(callback); //trigger callback function once data is loaded

	function callback(error, csvData, brasilData){
		var states = topojson.feature(brasilData, brasilData.objects.estados);
        dadosOlac = csvData;
        dadosGeo = states;
        
        //AGREGAÇÃO DO SOMATÓRIO DE VOLUME POR UNIDADE DA FEDERAÇÃO
        var listUF = [];
        
        states.features.forEach(function (d) {listUF.push(d.id)});
            
            csvData.forEach(function(d){
            d.volume = parseInt(d.volume);

        });
        
        var aggVolume = d3.nest()
            .key(function(d) { return d.uf })
            .rollup(function (v){ 
                return d3.sum(v, function(data){
                                return data.volume; 
                })
            })
            .entries(dadosOlac);

        totalVolume = aggVolume


        var aggPorCategoria = d3.nest()
            .key(function(d) { return d.category })
			.key(function(d) { return d.uf})
            .rollup(function (v){ 
                return d3.sum(v, function(data){
                                return data.volume; 
                            })
            })
            .entries(dadosOlac);

        totalPorCategoria = aggPorCategoria;
        totalPorCategoria[0]['key'] = "Engrenagens e Sistemas Circulatórios"
        totalPorCategoria[8]['key'] = "Transmissões e Sistemas Hidráulicos"

        //ARMAZENAR TODAS AS CATEGORIAS DE ÓLEO LUBRIFICANTE ACABADO
        var nomeCategoriaOlac = [];

        
        totalPorCategoria.forEach(function (d) {
            nomeCategoriaOlac.push(d.key)
        
        });


        for (var i=0; i<totalVolume.length; i++) {		
            var volumeUF = totalVolume[i]; // DADOS REFERENTE A UM ESTADO
            var strUF = volumeUF.key;  // ARMAZENA A UF DO REFERIDO ESTADO
                
        	//ITERAR SOBRE OS ESTADOS PARA INSERIR OS DADOS DE PRODUÇÃO PARA
            //CADA UNIDADE DA FEDERAÇÃO.
			for (var a=0; a<states.features.length; a++){
            //CHECAR SE O ID DO ARQUIVO JSON É ATRIBUÍDO A UF DE TOTALVOLUME		
    				if (states.features[a].id == strUF){
                            states.features[a].properties['Volume Total OLAC'] = volumeUF.values;            
                    }
            
            }
            
        };

        //AGREGAR DADOS PARA ESTADOS COM PRODUÇÃO E SEM PRODUÇÃO DE OLAC
        var uf_producao = [];
        var uf_sproducao = [];

        totalVolume.forEach(function(v) {
            uf_producao.push(v.key) // ADICIONA A UF AO RESPECTIVO ARRAY
        });

        listUF.forEach(function(v){
            if (uf_producao.indexOf(v) == -1) { // IDENTICA AS UF'S QUE NÃO ESTÃO
                uf_sproducao.push(v)            // NA LISTA DE ESTADOS PRODUTORES
            }                                   // E DEPOIS INSERE NO ARRAY

        });

        //PARA CADA ESTADO NÃO PRODUTOR DE OLAC, ADICIONA UM VALOR DE PRODUCAO 0
        uf_sproducao.forEach(function(d) {
            for(var i = 0; i< states.features.length; i++) {
                if(states.features[i].id == d) {
                     states.features[i].properties['Volume Total OLAC'] = 0;
                }
            }
        });

        for (var i=0; i<totalPorCategoria.length; i++) {		
            var dadoCategoria = totalPorCategoria[i]; // DADOS REFERENTE A UMA CATEGORIA
            var nomeCategoria = dadoCategoria.key;  // ARMAZENA O NOME DA CATEGORIA

            //ITERAR SOBRE OS ESTADOS QUE POSSUEM PRODUCAO DE UMA DADA CATEGORIA

            dadoCategoria.values.forEach(function(v){          

                //ITERAR SOBRE OS ESTADOS PARA INSERIR OS DADOS DE PRODUÇÃO POR
                //CATEGORIA
                for (var a=0; a<states.features.length; a++){
                //CHECAR SE O ID DO ARQUIVO JSON É ATRIBUÍDO A UF DE dadoCategoria		
                        if (states.features[a].id == v.key){
                            states.features[a].properties[nomeCategoria] = v.values;            
                        };
                
                };
            
            });
        };
        //ITERAR PELOS ESTADOS DO ARQUIVO JSON E INSERIR UM VALOR DE 0
        //PARA AS CATEGORIAS QUE NÃO POSSUEM PRODUCAO.
        nomeCategoriaOlac.forEach(function(n) {
            for (var a=0; a<states.features.length; a++){ 
                if (n in states.features[a].properties){
                    continue          
                } else {
                    states.features[a].properties[n] = 0; 
                }
                
            }

        });

        // Setup the scale and translate
        var b, s, t;
        projection.scale(1).translate([0, 0]);

        /* "The bounding box is represented by a two-dimensional array: [[left, bottom],
        [right, top]], where left is the minimum longitude, bottom is the minimum latitude,
        right is maximum longitude, and top is the maximum latitude." 
        
        bounding box = [ [minimum_longitude, minimum_latitude] , 
                         [maximum_longitude,maximum_latitude] ]

        */
        var b = path.bounds(states);
                
        /*
        scale =   Math.max( (maximum_longitude - minimum_longitude) / width ,
                        (maximum_latitude - minimum_latitude) / heigth )

        The value 95 adjusts the scale, because we are giving the map a bit of a breather
        on the edges in order to not have the paths intersect the edges of the SVG container
        item, basically reducing the scale by 5 percent.
        */
        var s = .95 / Math.max((b[1][0] - b[0][0]) / width, (b[1][1] - b[0][1]) / height);
                
        /* As we saw in Chapter 2, Creating Images from Simple Text, when we scale in SVG,
        it scales all the attributes (even x and y). In order to return the map to the center
        of the screen, we will use the translate function.

        The translate function receives an array with two parameters: the amount to
        translate in x, and the amount to translate in y. We will calculate x by fnding
        the center (topRight – topLeft)/2 and multiplying it by the scale. The result is then
        subtracted from the width of the SVG element.

        Our y translation is calculated similarly but using the bottomRight – bottomLeft values
        divided by 2, multiplied by the scale, then subtracted from the height.
        */
                
        var t = [(width - s * (b[1][0] + b[0][0])) / 2, (height - s * (b[1][1] + b[0][1])) / 2];
        projection.scale(s).translate(t);

        var brazil = void 0; // VARIÁVEL QUE SERÁ UTILIZADA PARA ARMAZENAR OS DADOS GEOGRÁFICOS
        var map = svg.append('g').attr('class', 'boundary');
        brazil = map.selectAll('path').data(states.features);
        recolorMap = colorScale(dadosGeo, variavelAlvo); //retrieve color scale generator

        //Enter
        brazil.enter()
            .append('path')
            .attr('d', path)
            .attr("class", function(d) {return d.id + " estado";})
            .style("fill", function(d){ return choropleth(d,recolorMap)})
            .on("mouseover", highlight)
            .on("mouseout", dehighlight)
            .on("mousemove", moveLabel)
            .append("desc")
            .text(function(d){return choropleth(d,recolorMap)});

        svg.selectAll('text')
            .data(states.features)
            .enter()
            .append('text')
            .text(function(d) { return d.id; })
            .attr({
                    x: function(d) { return path.centroid(d)[0]; },
                    y: function(d) { return path.centroid(d)[1]; },
                                    'text-anchor': 'middle',
                                    'font-size': '10pt',
                                    'fill' : "black"
        });

        criarMenu(dadosOlac);
        legend(variavelAlvo, dadosGeo);
        



    };

};
//FUNÇÃO PARA ORGANIZAR UM ARRAY DE FORMA CRESCENTE
function compare(a, b){
    let comparison = 0;

    if (a > b) {
        comparison = 1;
    } else if (b > a) {
        comparison = -1;
    }

    return comparison;
}

function title_legend() {
    d3.select("#legenda_placeholder")
        .append("text")
        .attr("x", "50")
        .attr("y", "50")
        .style("font-family", "Inconsolata")
        .style("font-size", "20px")
        .attr("transform", "translate(-25, 75)")
        .text("Volumes de Produção / m³")




}
function legend(variavelAlvo, dadosGeo){
 
    var colorScale = d3.scale.quantize()
            .range(colorbrewer.Blues[9]);
        
    var domainArray = [];
    dadosGeo.features.forEach(function(v){
        domainArray.push(v.properties[variavelAlvo])
    })

    domainArray.sort(compare)

    colorScale.domain(domainArray)

    if(d3.select("#legenda_mapa").html() !== "") {

        d3.select("#legenda_mapa").html("")

        var svg = d3.select("#legenda_mapa").append("svg")
                .attr("width", "400")
                .attr("height", "800")
                .attr("id", "legenda_placeholder")


        var colorLegend = d3.legend.color()
            .labelFormat(myFormatter)
            .scale(colorScale)
            .shapePadding(10)
            .shapeWidth(20)
            .shapeHeight(20)
            .labelOffset(10)

        svg.append("g")
            .attr("transform", "translate(50, 150)")
            .call(colorLegend);

        title_legend()


    } else {
            var svg = d3.select("#legenda_mapa").append("svg")
                .attr("width", "400")
                .attr("height", "800")
                .attr("id", "legenda_placeholder")


            var colorLegend = d3.legend.color()
                .labelFormat(myFormatter)
                .scale(colorScale)
                .shapePadding(10)
                .shapeWidth(20)
                .shapeHeight(20)
                .labelOffset(10)

            svg.append("g")
                .attr("transform", "translate(50, 150)")
                .call(colorLegend);

        title_legend()

    }





}

function colorScale(dadosGeo, variavelAlvo) {

    //CRIAR UMA ESCALA DE CORES BASEADA EM QUANTIS
    var quantileScale = d3.scale.quantile()
    .range(colorbrewer.Blues[9])
    //To determine the quantile class breaks properly, the domain array must include 
    //all of the attribute values for the currently expressed attribute 
    //(note: an equal-interval classification can be created by instead passing 
    //a two-value array to domain() with just the minimum and maximum values of the expressed attribute). 

    var domainArray = [];
    dadosGeo.features.forEach(function(v){
        domainArray.push(v.properties[variavelAlvo])
    })
    domainArray.sort(compare)
    quantileScale.domain(domainArray);
    return quantileScale;
};

function choropleth(d, recolorMap){
    if(d instanceof Array){
        //OBTER O VALOR ATRIBUÍDO A VARIÁVEL
        d.forEach(function(v){
            var value = v.properties[variavelAlvo]
            if(value) {
                return recolorMap(value);
            } else {
                return d3.rgb(247,251,255);
            }
        })
    } else {
        var value = d.properties[variavelAlvo]
            if(value) {
                return recolorMap(value);
            } else {
                return d3.rgb(247,251,255);
            }
    }
};  

function criarMenu(dadosOlac){
    var menu = d3.select("#menu")
                .html("<h3>Selecione a Categoria</h3>")
                .append("select")
                .on("change", function() {
                    mudarVariavel(this.value, dadosGeo);
                    legend(this.value, dadosGeo);
                });

    menu.selectAll("options")
        .data(listaVariaveis)
        .enter()
        .append("option")
        .attr("value", function(d){return d})
        .text(function(d) { 
            return d });

}

function mudarVariavel(variavel,dadosGeo) {
    variavelAlvo = variavel;
    d3.selectAll("path.estado")
        .style("fill",function(d){return choropleth(d, colorScale(dadosGeo,variavelAlvo))})
        .select("desc")
        .text(function(d){ return choropleth(d, colorScale(dadosGeo,variavelAlvo))})


};

function highlight(data){
    
    var id_estado = data.id
    var prop_estado = data.properties
    d3.select("."+id_estado) // SELECIONA O ESTADO NO DOM
        .style("fill", "#FF9900")
    //CONTEÚDO DA LEGENDA
    var nome_legenda = prop_estado.nome;
    var stringVolume = String(myFormatter(prop_estado[variavelAlvo]))
    var conteudo_legenda = "<h1>"+stringVolume+" m³"+"</h1><br>"
    

    //DIV PARA RECEBER A LEGENDA
    var legenda = d3.select("#container")
                    .append("div")
                    .attr("class", "legenda")
                    .attr("id", id_estado+"legenda")
                    .html(conteudo_legenda)
                    .append("div")
                    .attr("class","nomelegenda")
                    .html("Volume de Produção de OLAC");

    

};

function dehighlight(data){
    var id_estado = data.id
    var prop_estado = data.properties
    var estado = d3.select("."+id_estado)
    var adicionarCor = estado.select("desc").text();
    estado.style("fill", adicionarCor)
    estado.style("fill-opacity", 1)
    d3.select("#"+id_estado+"legenda").remove()
    
};

function moveLabel() {

    var x = d3.event.clientX; //horizontal label coordinate
    var y = d3.event.clientY; //vertical label coordinate
		
    d3.select(".legenda") //select the label div for moving
        .style("margin-left", x+"px") //reposition label horizontal
        .style("margin-top", y+"px"); //reposition label vertical
};


