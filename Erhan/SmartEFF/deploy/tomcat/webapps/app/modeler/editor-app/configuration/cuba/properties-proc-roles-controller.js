var KisBpmProcRolesCtrl = [ '$scope', '$modal', '$timeout', '$translate', function($scope, $modal) {

    // Config for the modal window
    var opts = {
        template:  'editor-app/configuration/properties/cuba/proc-roles-popup.html?version=' + Date.now(),
        scope: $scope
    };

    // Open the dialog
    $modal(opts);
}];

var KisBpmProcRolesPopupCtrl = ['$scope', '$q', '$translate', function($scope, $q, $translate) {

    // Put json representing proc roles on scope
    if ($scope.property.value !== undefined && $scope.property.value !== null && $scope.property.value.length > 0) {

        if ($scope.property.value.constructor == String) {
            $scope.procRoles = JSON.parse($scope.property.value);
        } else {
            // Note that we clone the json object rather then setting it directly,
            // this to cope with the fact that the user can click the cancel button and no changes should have happended
            $scope.procRoles = angular.copy($scope.property.value);
        }
    } else {
        $scope.procRoles = [];
    }

    // Array to contain selected properties (yes - we only can select one, but ng-grid isn't smart enough)
    $scope.selectedProperties = [];

    $scope.translationsRetrieved = false;

    $scope.labels = {};

    var codePromise = $translate('PROPERTY.PROCROLES.CODE');
    var namePromise = $translate('PROPERTY.PROCROLES.NAME');

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
    //        selectedItems: $scope.selectedProperties,
    //        columnDefs: [{ field: 'code', displayName: $scope.labels.codeLabel },
    //            { field: 'name', displayName: $scope.labels.nameLabel}]
    //    };
    //}).catch(function(result) {
    //    console.print('Error');
    //});

    $scope.translationsRetrieved = true;
    $scope.gridOptions = {
        data: 'procRoles',
        enableRowReordering: true,
        headerRowHeight: 28,
        multiSelect: false,
        keepLastSelected: false,
        selectedItems: $scope.selectedProperties,
        columnDefs: [{field: 'code', displayName: 'Code'},
            {field: 'name', displayName: 'Name'}]
    }

        // Click handler for add button
    $scope.addNewProperty = function() {
        $scope.procRoles.push({ code : '', name : ''});
    };

    // Click handler for remove button
    $scope.removeProperty = function() {
        if ($scope.selectedProperties.length > 0) {
            var index = $scope.procRoles.indexOf($scope.selectedProperties[0]);
            $scope.gridOptions.selectItem(index, false);
            $scope.procRoles.splice(index, 1);

            $scope.selectedProperties.length = 0;
            if (index < $scope.procRoles.length) {
                $scope.gridOptions.selectItem(index + 1, true);
            } else if ($scope.procRoles.length > 0) {
                $scope.gridOptions.selectItem(index - 1, true);
            }
        }
    };

    //// Click handler for up button
    //$scope.movePropertyUp = function() {
    //    if ($scope.selectedProperties.length > 0) {
    //        var index = $scope.formProperties.indexOf($scope.selectedProperties[0]);
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
    //    if ($scope.selectedProperties.length > 0) {
    //        var index = $scope.formProperties.indexOf($scope.selectedProperties[0]);
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

        if ($scope.procRoles.length > 0) {
            $scope.property.value = {};
            $scope.property.value = $scope.procRoles;
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