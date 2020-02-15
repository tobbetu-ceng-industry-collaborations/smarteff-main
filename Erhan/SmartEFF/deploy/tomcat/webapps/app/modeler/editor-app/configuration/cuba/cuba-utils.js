CubaStencilUtils = {
    fillMainAndAdvancedProperties: function(selectedItem, stencil) {
        selectedItem.mainProperties = [];
        selectedItem.advancedProperties = [];

        // if no mainPropertiesPackages section defined for the stencil in stencilset.json then all
        // properties should be in main group
        // otherwise fill two collections: mainProperties (defined in mainPropertiesPackages) and
        // advancedProperties (the others)
        if (stencil._mainPropertiesIds == undefined || stencil._mainPropertiesIds.length == 0) {
            selectedItem.mainProperties = selectedItem.properties;
        } else {
            selectedItem.properties.each(function (prop) {
                if (stencil._mainPropertiesIds.indexOf(prop.key) > -1) {
                    selectedItem.mainProperties.push(prop);
                } else {
                    selectedItem.advancedProperties.push(prop);
                }
            });
            selectedItem.properties = selectedItem.mainProperties.concat(selectedItem.advancedProperties);
        }
    }
}