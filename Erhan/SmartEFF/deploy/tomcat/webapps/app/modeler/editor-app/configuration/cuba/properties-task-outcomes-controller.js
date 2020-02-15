var KisBpmTaskOutcomesCtrl = [ '$scope', '$modal', '$timeout', '$translate', function($scope, $modal) {

    // Config for the modal window
    var opts = {
        template:  'editor-app/configuration/properties/cuba/task-outcomes-popup.html?version=' + Date.now(),
        scope: $scope
    };

    // Open the dialog
    $modal(opts);
}];

var KisBpmTaskOutcomesPopupCtrl = ['$scope', '$q', '$translate', '$http', '$timeout', function($scope, $q, $translate, $http, $timeout) {

    // Put json representing task outcomes on scope
    if ($scope.property.value !== undefined && $scope.property.value !== null && $scope.property.value.length > 0) {

        if ($scope.property.value.constructor == String) {
            $scope.taskOutcomes = JSON.parse($scope.property.value);
        } else {
            // Note that we clone the json object rather then setting it directly,
            // this to cope with the fact that the user can click the cancel button and no changes should have happended
            $scope.taskOutcomes = angular.copy($scope.property.value);
        }
    } else {
        $scope.taskOutcomes = [];
    }

    // Array to contain selected properties (yes - we only can select one, but ng-grid isn't smart enough)
    $scope.selectedOutcomes = [];
    $scope.selectedFormParams = [];

    $scope.translationsRetrieved = false;

    $scope.labels = {};

    var codePromise = $translate('PROPERTY.TASKOUTCOMES.CODE');
    var namePromise = $translate('PROPERTY.TASKOUTCOMES.NAME');

    //todo gorbunkov localization
    //$q.all([codePromise, namePromise]).then(function(results) {
    //	$scope.labels.codeLabel = results[0];
    //    $scope.labels.nameLabel = results[1];
    //    $scope.translationsRetrieved = true;
    //
    //	// Config for grid
    //    $scope.gridOptions = {
    //        data: 'procRoles',
    //        enableRowReordering: true,
    //        headerRowHeight: 28,
    //        multiSelect: false,
    //        keepLastSelected : false,
    //        selectedItems: $scope.selectedOutcomes,
    //        columnDefs: [{ field: 'code', displayName: $scope.labels.codeLabel },
    //            { field: 'name', displayName: $scope.labels.nameLabel}]
    //    };
    //}).catch(function(result) {
    //    console.print('Error');
    //});

    $scope.translationsRetrieved = true;
    $scope.gridOptions = {
        data: 'taskOutcomes',
        enableRowReordering: true,
        headerRowHeight: 28,
        multiSelect: false,
        keepLastSelected: false,
        selectedItems: $scope.selectedOutcomes,
        columnDefs: [{field: 'name', displayName: 'Name'}, {field: 'form.caption', displayName: 'Form'}]
    }

    $scope.propertiesGridOptions = {
        data: 'selectedOutcomes[0].form.params',
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

            $scope.$watch('selectedOutcomes[0].form.name', function(newValue) {
                for (var i = 0; i < $scope.formDescriptions.length; i++) {
                    var formDescription = $scope.formDescriptions[i];
                    if (formDescription.name == newValue) {
                        $scope.currentFormDescription = formDescription;
                        $scope.selectedOutcomes[0].form.caption = formDescription.caption;
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
    var propertyIndex = 1;
    $scope.addNewOutcome = function() {
        var name = "";
        var caption = "";
        if ($scope.defaultFormDescription != undefined) {
            name = $scope.defaultFormDescription.name;
            caption = $scope.defaultFormDescription.caption;
        }

        $scope.taskOutcomes.push({
            name : '',
            form: {name: name, caption: caption, params: []}});
    };

    // Click handler for remove button
    $scope.removeOutcome = function() {
        if ($scope.selectedOutcomes.length > 0) {
            var index = $scope.taskOutcomes.indexOf($scope.selectedOutcomes[0]);
            $scope.gridOptions.selectItem(index, false);
            $scope.taskOutcomes.splice(index, 1);

            $scope.selectedOutcomes.length = 0;
            if (index < $scope.taskOutcomes.length) {
                $scope.gridOptions.selectItem(index + 1, true);
            } else if ($scope.taskOutcomes.length > 0) {
                $scope.gridOptions.selectItem(index - 1, true);
            }
        }
    };

    $scope.addNewFormProperty = function() {
        $scope.selectedOutcomes[0].form.params.push({ name : '', value: ''});
    };

    // Click handler for remove button
    $scope.removeFormProperty = function() {
        if ($scope.selectedFormParams.length > 0) {
            var index = $scope.selectedOutcomes[0].form.params.indexOf($scope.selectedFormParams[0]);
            $scope.propertiesGridOptions.selectItem(index, false);
            $scope.selectedOutcomes[0].form.params.splice(index, 1);

            $scope.selectedFormParams.length = 0;
            //if (index < $scope.taskOutcomes.length) {
            //    $scope.gridOptions.selectItem(index + 1, true);
            //} else if ($scope.taskOutcomes.length > 0) {
            //    $scope.gridOptions.selectItem(index - 1, true);
            //}
        }
    };

    // Click handler for up button
    $scope.moveOutcomeUp = function() {
        if ($scope.selectedOutcomes.length > 0) {
            var index = $scope.taskOutcomes.indexOf($scope.selectedOutcomes[0]);
            if (index != 0) { // If it's the first, no moving up of course
                // Reason for funny way of swapping, see https://github.com/angular-ui/ng-grid/issues/272
                var temp = $scope.taskOutcomes[index];
                $scope.taskOutcomes.splice(index, 1);
                $timeout(function(){
                    $scope.taskOutcomes.splice(index + -1, 0, temp);
                }, 100);

            }
        }
    };

    // Click handler for down button
    $scope.moveOutcomeDown = function() {
        if ($scope.selectedOutcomes.length > 0) {
            var index = $scope.taskOutcomes.indexOf($scope.selectedOutcomes[0]);
            if (index != $scope.taskOutcomes.length - 1) { // If it's the last element, no moving down of course
                // Reason for funny way of swapping, see https://github.com/angular-ui/ng-grid/issues/272
                var temp = $scope.taskOutcomes[index];
                $scope.taskOutcomes.splice(index, 1);
                $timeout(function(){
                    $scope.taskOutcomes.splice(index + 1, 0, temp);
                }, 100);

            }
        }
    };

    // Click handler for save button
    $scope.save = function() {

        if ($scope.taskOutcomes.length > 0) {
            $scope.property.value = {};
            $scope.property.value = $scope.taskOutcomes;
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