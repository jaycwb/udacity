function pieChart() {
        var svg = dimple.newSvg("#pieContainer", 900, 400);
        d3.csv("/data/producao_categoria_m3.csv", function (data) {
                var myChart = new dimple.chart(svg, data);
                myChart.setBounds(20, 20, 560, 360)
                myChart.addMeasureAxis("p", "Volume");
                var ring = myChart.addSeries("Categoria", dimple.plot.pie);
                ring.innerRadius = "50%";
                myChart.addLegend(500, 20, 50, 400, "left");
                myChart.draw();
            });

}

function barChart() {
        var svg = dimple.newSvg("#barContainer", 700, 550);
        d3.csv("/data/producao_vs_vendas.csv", function (data) {
                var myChart = new dimple.chart(svg, data);
                myChart.setBounds(20, 20, 560, 360)
                var x = myChart.addCategoryAxis("x", "Categoria");
                var y = myChart.addMeasureAxis("y", "Percentual");
                bars = myChart.addSeries(null, dimple.plot.bar);
                bars.barGap = 0.5;
                myChart.draw();

        x.shapes.selectAll("text").attr("transform",
        function (d) { return d3.select(this).attr("transform") + " translate(0, 20) rotate(-45)";
    });
        d3.select("#barContainer").select(".dimple-chart").attr("transform", "translate(10,0)");
        bar = d3.select("#barContainer").select("svg")
                .append("line")
                .attr("y1", y._scale(1))
                .attr("y2", y._scale(1))
                .attr("x1", myChart._yPixels()+10)
                .attr("x2", myChart._yPixels() + myChart._heightPixels() + 210)
                .style("stroke", "red")
                .style("stroke-dasharray", "4");

        d3.select("#barContainer")
            .select("svg")
            .select("#dimple-all-ciclo-diesel---")
            .style("fill", "red");
        d3.select("#barContainer")
            .select("svg")
            .select("#dimple-all-ciclo-otto---")
            .style("fill", "red");

        d3.select("#barContainer")
            .select("svg")
            .select("#dimple-all--leos-lubrificantes-mar-timos---")
            .style("fill", "black")
            .style("opacity", "0.15")
            .style("stroke", "black")    

        d3.select("#barContainer")
            .select("svg")
            .select("#dimple-all--leos-lubrificantes-ferrovi-rios---")
            .style("fill", "black")
            .style("opacity", "0.15")
            .style("stroke", "black")         

        d3.select("#barContainer")
            .select("svg")
            .select("#dimple-all-motores-2-tempos---")
            .style("fill", "black")
            .style("opacity", "0.15")
            .style("stroke", "black")  

        d3.select("#barContainer")
            .select("svg")
            .select("#dimple-all-transmiss-es-e-sistemas-hidr-ulicos---")
            .style("fill", "black")
            .style("opacity", "0.15")
            .style("stroke", "black")  

        d3.select("#barContainer")
            .select("svg")
            .select("#dimple-all-engrenagens-e-sistemas-circulat-rios---")
            .style("fill", "black")
            .style("opacity", "0.15")
            .style("stroke", "black")  

        d3.select("#barContainer")
            .select("svg")
            .select("#dimple-all-isolante-tipo-a---")
            .style("fill", "black")
            .style("opacity", "0.15")
            .style("stroke", "black")  

        d3.select("#barContainer")
            .select("svg")
            .select("#dimple-all-outros--leos-lubrificantes-acabados---")
            .style("fill", "black")
            .style("opacity", "0.15")
            .style("stroke", "black")  

        d3.select("#barContainer")
            .select("svg")
            .select("#dimple-all-isolante-tipo-b---")
            .style("fill", "black")
            .style("opacity", "0.15")
            .style("stroke", "black")  

         d3.select("#barContainer")
            .select("svg")
            .select("#dimple-all--leos-lubrificantes-para-avia--o---")
            .style("fill", "black")
            .style("opacity", "0.15")
            .style("stroke", "black")  
        });
}
