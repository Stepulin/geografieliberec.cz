ol.proj.proj4.register(proj4);
ol.proj.get("EPSG:4326").setExtent([-180.000000, -55.918504, 180.000000, 83.634101]);
var wms_layers = [];

var format_hustotazalidneni2019_0 = new ol.format.GeoJSON();
var features_hustotazalidneni2019_0 = format_hustotazalidneni2019_0.readFeatures(json_hustotazalidneni2019_0, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:4326'});
var jsonSource_hustotazalidneni2019_0 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_hustotazalidneni2019_0.addFeatures(features_hustotazalidneni2019_0);
var lyr_hustotazalidneni2019_0 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_hustotazalidneni2019_0, 
                style: style_hustotazalidneni2019_0,
                interactive: true,
    title: 'hustota zalidneni 2019<br />\
    <img src="styles/legend/hustotazalidneni2019_0_0.png" /> 39 a méně<br />\
    <img src="styles/legend/hustotazalidneni2019_0_1.png" /> 40 - 89<br />\
    <img src="styles/legend/hustotazalidneni2019_0_2.png" /> 90 - 219<br />\
    <img src="styles/legend/hustotazalidneni2019_0_3.png" /> 220 a více<br />'
        });

lyr_hustotazalidneni2019_0.setVisible(true);
var layersList = [lyr_hustotazalidneni2019_0];
lyr_hustotazalidneni2019_0.set('fieldAliases', {'ADMIN': 'ADMIN', 'rok 2019': 'rok 2019', });
lyr_hustotazalidneni2019_0.set('fieldImages', {'ADMIN': 'TextEdit', 'rok 2019': 'TextEdit', });
lyr_hustotazalidneni2019_0.set('fieldLabels', {'ADMIN': 'no label', 'rok 2019': 'no label', });
lyr_hustotazalidneni2019_0.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});