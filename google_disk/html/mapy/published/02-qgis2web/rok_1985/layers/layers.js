ol.proj.proj4.register(proj4);
ol.proj.get("EPSG:4326").setExtent([-180.000000, -55.918504, 180.000000, 83.634101]);
var wms_layers = [];

var format_hustotazalidneni1985_0 = new ol.format.GeoJSON();
var features_hustotazalidneni1985_0 = format_hustotazalidneni1985_0.readFeatures(json_hustotazalidneni1985_0, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:4326'});
var jsonSource_hustotazalidneni1985_0 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_hustotazalidneni1985_0.addFeatures(features_hustotazalidneni1985_0);
var lyr_hustotazalidneni1985_0 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_hustotazalidneni1985_0, 
                style: style_hustotazalidneni1985_0,
                interactive: true,
    title: 'hustota zalidneni 1985<br />\
    <img src="styles/legend/hustotazalidneni1985_0_0.png" /> 19 a méně<br />\
    <img src="styles/legend/hustotazalidneni1985_0_1.png" /> 20 - 59<br />\
    <img src="styles/legend/hustotazalidneni1985_0_2.png" /> 60 - 129<br />\
    <img src="styles/legend/hustotazalidneni1985_0_3.png" /> 130 a více<br />'
        });

lyr_hustotazalidneni1985_0.setVisible(true);
var layersList = [lyr_hustotazalidneni1985_0];
lyr_hustotazalidneni1985_0.set('fieldAliases', {'ADMIN': 'ADMIN', 'rok 1985': 'rok 1985', });
lyr_hustotazalidneni1985_0.set('fieldImages', {'ADMIN': 'TextEdit', 'rok 1985': 'TextEdit', });
lyr_hustotazalidneni1985_0.set('fieldLabels', {'ADMIN': 'no label', 'rok 1985': 'no label', });
lyr_hustotazalidneni1985_0.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});