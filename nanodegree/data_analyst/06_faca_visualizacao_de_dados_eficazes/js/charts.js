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
                myChart.addSeries(null, dimple.plot.bar);
                myChart.draw();
        bar = d3.select("#barContainer").select("svg")
                .append("line")
                .attr("y1", y._scale(1))
                .attr("y2", y._scale(1))
                .attr("x1", myChart._yPixels())
                .attr("x2", myChart._yPixels() + myChart._heightPixels() + 200)
                .style("stroke", "red")
                .style("stroke-dasharray", "3");
        });
}
