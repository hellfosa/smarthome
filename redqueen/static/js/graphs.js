        $(document).ready(function () {

          var ctx = document.getElementById("myChart").getContext('2d');
          period = [];
          temp = [];
          humi = [];
          $.getJSON("/graphs", {'query': 'iwantgraphs', 'range': 'day', 'room': 'master_bedroom'}, function (results) {
              $.each(results, function (json, element) {
                    if (element.channel == "/climate/master_bedroom/temperature") {
                        temp.push(element.signal);
                    } else if (element.channel == "/climate/master_bedroom/humidity") {
                        humi.push(element.signal);
                    }
                    period.push(element.published);

              });

          datasets = [{
                    data: temp,
                    label: "Temperature",
                    borderColor: "#3e95cd",
                    fill: false
                  }, {
                    data: humi,
                    label: "Humidity",
                    borderColor: "#c45850",
                    fill: false
                  }
                ];
          myChart.data.labels = period;
          myChart.data.datasets = datasets;
          myChart.update();
         });


            var myChart = new Chart(ctx, {
              type: 'line',
              data: {
                labels: 0,
                datasets: [{
                    data: 0,
                    label: "Temperature",
                    borderColor: "#3e95cd",
                    fill: false
                  }, {
                    data: 0,
                    label: "Humidity",
                    borderColor: "#c45850",
                    fill: false
                  }
                ]
              },
              options: {
                title: {
                  display: true,
                  text: 'Climate stats in master bedroom'
                }
              }
            });
          });

