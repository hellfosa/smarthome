Morris.Area({
    element: 'morris-area-chart2',
    data: [{
        period: '2010',
        SiteA: 0,
        SiteB: 0,
        SiteC: 15,

    }, {
        period: '2011',
        SiteA: 130,
        SiteB: 100,
        SiteC: 19,

    }, {
        period: '2012',
        SiteA: 80,
        SiteB: 60,
        SiteC: 195,

    }, {
        period: '2013',
        SiteA: 70,
        SiteB: 200,
        SiteC: 125,

    }, {
        period: '2014',
        SiteA: 180,
        SiteB: 150,
        SiteC: 44,

    }, {
        period: '2015',
        SiteA: 105,
        SiteB: 90,
        SiteC: 15,

    }, {
        period: '2016',
        SiteA: 250,
        SiteB: 150,
        SiteC: 0,

    }],
    xkey: 'period',
    ykeys: ['SiteA', 'SiteB', 'SiteC'],
    labels: ['Site A', 'Site B', 'Site C'],
    pointSize: 0,
    fillOpacity: 0.7,
    pointStrokeColors: ['#ccc', '#cbb2ae'],
    behaveLikeLine: true,
    gridLineColor: '#e0e0e0',
    lineWidth: 0,
    smooth: false,
    hideHover: 'auto',
    lineColors: ['#ccc', '#cbb2ae'],
    resize: true

});

$(".counter").counterUp({
    delay: 100,
    time: 1200
});
