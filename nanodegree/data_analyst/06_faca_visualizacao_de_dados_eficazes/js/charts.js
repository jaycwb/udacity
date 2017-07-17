function pieChart() {
        var svg = dimple.newSvg("#chartContainer", 900, 400);
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
