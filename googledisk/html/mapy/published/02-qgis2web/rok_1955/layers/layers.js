ol.proj.proj4.register(proj4);
ol.proj.get("EPSG:4326").setExtent([-180.000000, -55.918504, 180.000000, 83.634101]);
var wms_layers = [];

var format_hustotazalidneni1955_0 = new ol.format.GeoJSON();
var features_hustotazalidneni1955_0 = format_hustotazalidneni1955_0.readFeatures(json_hustotazalidneni1955_0, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:4326'});
var jsonSource_hustotazalidneni1955_0 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_hustotazalidneni1955_0.addFeatures(features_hustotazalidneni1955_0);
var lyr_hustotazalidneni1955_0 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_hustotazalidneni1955_0, 
                style: style_hustotazalidneni1955_0,
                interactive: true,
    title: 'hustota zalidneni 1955<br />\
    <img src="styles/legend/hustotazalidneni1955_0_0.png" /> 9 a méně<br />\
    <img src="styles/legend/hustotazalidneni1955_0_1.png" /> 10 - 29<br />\
    <img src="styles/legend/hustotazalidneni1955_0_2.png" /> 30 - 79<br />\
    <img src="styles/legend/hustotazalidneni1955_0_3.png" /> 80 a více<br />'
        });

lyr_hustotazalidneni1955_0.setVisible(true);
var layersList = [lyr_hustotazalidneni1955_0];
lyr_hustotazalidneni1955_0.set('fieldAliases', {'ADMIN': 'ADMIN', 'rok 1955': 'rok 1955', });
lyr_hustotazalidneni1955_0.set('fieldImages', {'ADMIN': 'TextEdit', 'rok 1955': 'TextEdit', });
lyr_hustotazalidneni1955_0.set('fieldLabels', {'ADMIN': 'no label', 'rok 1955': 'no label', });
lyr_hustotazalidneni1955_0.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});