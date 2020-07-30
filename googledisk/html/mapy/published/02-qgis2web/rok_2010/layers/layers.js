ol.proj.proj4.register(proj4);
ol.proj.get("EPSG:4326").setExtent([-180.000000, -55.918504, 180.000000, 83.634101]);
var wms_layers = [];

var format_hustotazalidneni2010_0 = new ol.format.GeoJSON();
var features_hustotazalidneni2010_0 = format_hustotazalidneni2010_0.readFeatures(json_hustotazalidneni2010_0, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:4326'});
var jsonSource_hustotazalidneni2010_0 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_hustotazalidneni2010_0.addFeatures(features_hustotazalidneni2010_0);
var lyr_hustotazalidneni2010_0 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_hustotazalidneni2010_0, 
                style: style_hustotazalidneni2010_0,
                interactive: true,
    title: 'hustota zalidneni 2010<br />\
    <img src="styles/legend/hustotazalidneni2010_0_0.png" /> 34 a méně<br />\
    <img src="styles/legend/hustotazalidneni2010_0_1.png" /> 35 - 79<br />\
    <img src="styles/legend/hustotazalidneni2010_0_2.png" /> 80 - 189<br />\
    <img src="styles/legend/hustotazalidneni2010_0_3.png" /> 190 a více<br />'
        });

lyr_hustotazalidneni2010_0.setVisible(true);
var layersList = [lyr_hustotazalidneni2010_0];
lyr_hustotazalidneni2010_0.set('fieldAliases', {'ADMIN': 'ADMIN', 'rok 2010': 'rok 2010', });
lyr_hustotazalidneni2010_0.set('fieldImages', {'ADMIN': 'TextEdit', 'rok 2010': 'TextEdit', });
lyr_hustotazalidneni2010_0.set('fieldLabels', {'ADMIN': 'no label', 'rok 2010': 'no label', });
lyr_hustotazalidneni2010_0.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});