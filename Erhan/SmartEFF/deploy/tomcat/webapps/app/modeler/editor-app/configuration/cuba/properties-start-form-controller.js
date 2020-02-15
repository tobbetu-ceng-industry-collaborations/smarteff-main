var KisBpmStartFormCtrl = [ '$scope', '$modal', '$timeout', '$translate', function($scope, $modal) {

    // Config for the modal window
    var opts = {
        template:  'editor-app/configuration/properties/cuba/start-form-popup.html?version=' + Date.now(),
        scope: $scope
    };

    // Open the dialog
    $modal(opts);
}];

var KisBpmStartFormPopupCtrl = ['$scope', '$q', '$translate', '$http', function($scope, $q, $translate, $http) {

    // Put json representing task outcomes on scope
    if ($scope.property.value !== undefined && $scope.property.value !== null && $scope.property.value != "") {

        if ($scope.property.value.constructor == String) {
            $scope.form = JSON.parse($scope.property.value);
        } else {
            // Note that we clone the json object rather then setting it directly,
            // this to cope with the fact that the user can click the cancel button and no changes should have happended
            $scope.form = angular.copy($scope.property.value);
        }
    }

    // Array to contain selected properties (yes - we only can select one, but ng-grid isn't smart enough)
    $scope.selectedFormParams = [];

    $scope.translationsRetrieved = false;

    $scope.labels = {};

    var codePromise = $translate('PROPERTY.TASKOUTCOMES.CODE');
    var namePromise = $translate('PROPERTY.TASKOUTCOMES.NAME');

    $scope.translationsRetrieved = true;

    $scope.gridOptions = {
        data: 'form.params',
        enableRowReordering: true,
        headerRowHeight: 28,
        multiSelect: false,
        keepLastSelected: false,
        selectedItems: $scope.selectedFormParams,
        columnDefs: [{field: 'name', displayName: 'Name'}, {field: 'value', displayName: 'Value'}]
    }

    $http.get(KISBPM.URL.getAllForms())
        .success(function(data) {
            $scope.formDescriptions = data;

            for (var i = 0; i < $scope.formDescriptions.length; i++) {
                var formDescription = $scope.formDescriptions[i];
                if (formDescription.isDefault === true) {
                    $scope.defaultFormDescription = formDescription;
                    break;
                }
            }

            //init form if it isn't filled yet
            if ($scope.form == undefined) {
                var name = "";
                var caption = "";
                if ($scope.defaultFormDescription != undefined) {
                    name = $scope.defaultFormDescription.name;
                    caption = $scope.defaultFormDescription.caption;
                }
                $scope.form = {name: name, caption: caption, params: []};
            }

            $scope.$watch('form.name', function(newValue) {
                for (var i = 0; i < $scope.formDescriptions.length; i++) {
                    var formDescription = $scope.formDescriptions[i];
                    if (formDescription.name == newValue) {
                        $scope.currentFormDescription = formDescription;
                        $scope.form.caption = formDescription.caption;
                        break;
                    }
                }
            });
        })
        .error(function(data) {

        });

    $scope.setDefaultParamValue = function() {
        var params = $scope.currentFormDescription.params;
        for (var i = 0; i < params.length; i++) {
            var paramDescription = params[i];
            if (paramDescription.name == $scope.selectedFormParams[0].name) {
                $scope.selectedFormParams[0].value = paramDescription.value;
                break;
            }
        }
    };

        // Click handler for add button
    $scope.addNewFormProperty = function() {
        $scope.form.params.push({ name : '', value: ''});
    };

    // Click handler for remove button
    $scope.removeFormProperty = function() {
        if ($scope.selectedFormParams.length > 0) {
            var index = $scope.form.params.indexOf($scope.selectedFormParams[0]);
            $scope.gridOptions.selectItem(index, false);
            $scope.form.params.splice(index, 1);

            $scope.selectedFormParams.length = 0;
        }
    };

    //// Click handler for up button
    //$scope.movePropertyUp = function() {
    //    if ($scope.selectedOutcomes.length > 0) {
    //        var index = $scope.formProperties.indexOf($scope.selectedOutcomes[0]);
    //        if (index != 0) { // If it's the first, no moving up of course
    //            // Reason for funny way of swapping, see https://github.com/angular-ui/ng-grid/issues/272
    //            var temp = $scope.formProperties[index];
    //            $scope.formProperties.splice(index, 1);
    //            $timeout(function(){
    //                $scope.formProperties.splice(index + -1, 0, temp);
    //            }, 100);
    //
    //        }
    //    }
    //};
    //
    //// Click handler for down button
    //$scope.movePropertyDown = function() {
    //    if ($scope.selectedOutcomes.length > 0) {
    //        var index = $scope.formProperties.indexOf($scope.selectedOutcomes[0]);
    //        if (index != $scope.formProperties.length - 1) { // If it's the last element, no moving down of course
    //            // Reason for funny way of swapping, see https://github.com/angular-ui/ng-grid/issues/272
    //            var temp = $scope.formProperties[index];
    //            $scope.formProperties.splice(index, 1);
    //            $timeout(function(){
    //                $scope.formProperties.splice(index + 1, 0, temp);
    //            }, 100);
    //
    //        }
    //    }
    //};

    // Click handler for save button
    $scope.save = function() {

        if ($scope.form.name != null) {
            $scope.property.value = {};
            $scope.property.value = $scope.form;
        } else {
            $scope.property.value = null;
        }

        $scope.updatePropertyInModel($scope.property);
        $scope.close();
    };

    $scope.cancel = function() {
    	$scope.$hide();
    	$scope.property.mode = 'read';
    };

    // Close button handler
    $scope.close = function() {
    	$scope.$hide();
    	$scope.property.mode = 'read';
    };

}];