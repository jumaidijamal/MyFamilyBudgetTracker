<canvas id="categoryChart"></canvas>

fetch("/api/dashboard/category")
.then(r => r.json())
.then(data => {

    new Chart(
        document.getElementById(
            "categoryChart"
        ),
        {
            type: "pie",

            data: {
                labels: data.labels,

                datasets: [
                    {
                        data: data.values
                    }
                ]
            }
        }
    );

});