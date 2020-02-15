/*
 * Activiti Modeler component part of the Activiti project
 * Copyright 2005-2014 Alfresco Software, Ltd. All rights reserved.
 * 
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.

 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 */

/**
 * SaveModel action is overriden because save dialog is unnecessary.
 * We need to save model immediately.
 * Method body is a modified copy of save function from SaveModelCtrl
 */
KISBPM.TOOLBAR.ACTIONS["saveModel"] = function(services) {
    var $scope = services.$scope;
    var modelMetaData = $scope.editor.getModelMetaData();
    var json = $scope.editor.getJSON();
    json = JSON.stringify(json);

    var params = {
        modeltype: modelMetaData.model.modelType,
        json_xml: json,
        name: 'model'
    };

    var selection = $scope.editor.getSelection();
    $scope.editor.setSelection([]);

    // Get the serialized svg image source
    var svgClone = $scope.editor.getCanvas().getSVGRepresentation(true);
    $scope.editor.setSelection(selection);
    if ($scope.editor.getCanvas().properties["oryx-showstripableelements"] === false) {
        var stripOutArray = jQuery(svgClone).find(".stripable-element");
        for (var i = stripOutArray.length - 1; i >= 0; i--) {
            stripOutArray[i].remove();
        }
    }

    // Remove all forced stripable elements
    var stripOutArray = jQuery(svgClone).find(".stripable-element-force");
    for (var i = stripOutArray.length - 1; i >= 0; i--) {
        stripOutArray[i].remove();
    }

    // Parse dom to string
    var svgDOM = DataManager.serialize(svgClone);

    modelMetaData.name = $scope.editor.getCanvas().properties['oryx-name'];
    modelMetaData.description = $scope.editor.getCanvas().properties['oryx-documentation'];

    var params = {
        json_xml: json,
        svg_xml: svgDOM,
        name: modelMetaData.name,
        description: modelMetaData.description
    };

    // Update
    services.$http({    method: 'PUT',
        data: params,
        ignoreErrors: true,
        headers: {'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
        transformRequest: function (obj) {
            var str = [];
            for (var p in obj) {
                str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
            }
            return str.join("&");
        },
        url: KISBPM.URL.putModel(modelMetaData.modelId)})

        .success(function (data, status, headers, config) {
            $scope.editor.handleEvents({
                type: ORYX.CONFIG.EVENT_SAVED
            });

//            $scope.status.loading = false;
//            $scope.$hide();

            // Fire event to all who is listening
            var saveEvent = {
                type: KISBPM.eventBus.EVENT_TYPE_MODEL_SAVED,
                model: params,
                modelId: modelMetaData.modelId,
                eventType: 'update-model'
            };
            KISBPM.eventBus.dispatch(KISBPM.eventBus.EVENT_TYPE_MODEL_SAVED, saveEvent);

            // Reset state
            $scope.error = undefined;
//            $scope.status.loading = false;

//            // Execute any callback
//            if (successCallback) {
//                successCallback();
//            }

        })
        .error(function (data, status, headers, config) {
            $scope.error = {};
            console.log('Something went wrong when updating the process model:' + JSON.stringify(data));
            $scope.status.loading = false;
        });
}


KISBPM.TOOLBAR.ACTIONS["closeEditor"] = function(services) {
    window.close();
}