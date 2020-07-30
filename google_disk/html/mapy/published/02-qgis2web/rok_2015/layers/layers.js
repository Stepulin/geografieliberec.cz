ol.proj.proj4.register(proj4);
ol.proj.get("EPSG:4326").setExtent([-180.000000, -55.918504, 180.000000, 83.634101]);
var wms_layers = [];

var format_hustotazalidneni2015_0 = new ol.format.GeoJSON();
var features_hustotazalidneni2015_0 = format_hustotazalidneni2015_0.readFeatures(json_hustotazalidneni2015_0, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:4326'});
var jsonSource_hustotazalidneni2015_0 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_hustotazalidneni2015_0.addFeatures(features_hustotazalidneni2015_0);
var lyr_hustotazalidneni2015_0 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_hustotazalidneni2015_0, 
                style: style_hustotazalidneni2015_0,
                interactive: true,
    title: 'hustota zalidneni 2015<br />\
    <img src="styles/legend/hustotazalidneni2015_0_0.png" /> 34 a méně<br />\
    <img src="styles/legend/hustotazalidneni2015_0_1.png" /> 35 - 84<br />\
    <img src="styles/legend/hustotazalidneni2015_0_2.png" /> 85 - 199<br />\
    <img src="styles/legend/hustotazalidneni2015_0_3.png" /> 200 a více<br />'
        });

lyr_hustotazalidneni2015_0.setVisible(true);
var layersList = [lyr_hustotazalidneni2015_0];
lyr_hustotazalidneni2015_0.set('fieldAliases', {'ADMIN': 'ADMIN', 'rok 2015': 'rok 2015', });
lyr_hustotazalidneni2015_0.set('fieldImages', {'ADMIN': 'TextEdit', 'rok 2015': 'TextEdit', });
lyr_hustotazalidneni2015_0.set('fieldLabels', {'ADMIN': 'no label', 'rok 2015': 'no label', });
lyr_hustotazalidneni2015_0.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});