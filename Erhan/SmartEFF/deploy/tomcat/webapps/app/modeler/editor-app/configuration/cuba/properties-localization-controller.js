var KisBpmLocalizationCtrl = [ '$scope', '$modal', '$timeout', '$translate', function($scope, $modal) {

    // Config for the modal window
    var opts = {
        template:  'editor-app/configuration/properties/cuba/localization-popup.html?version=' + Date.now(),
        scope: $scope
    };

    // Open the dialog
    $modal(opts);
}];

var KisBpmLocalizationPopupCtrl = ['$scope', '$q', '$translate', '$http', function($scope, $q, $translate, $http) {

    // Put json representing task outcomes on scope
    if ($scope.property.value !== undefined && $scope.property.value !== null && $scope.property.value.length > 0) {

        if ($scope.property.value.constructor == String) {
            $scope.messages = JSON.parse($scope.property.value);
        } else {
            // Note that we clone the json object rather then setting it directly,
            // this to cope with the fact that the user can click the cancel button and no changes should have happended
            $scope.messages = angular.copy($scope.property.value);
        }
    } else {
        $scope.messages = [];
    }

    $http.get(KISBPM.URL.getLocales())
        .success(function(data) {
            $scope.locales = data;
        }).error(function(data) {
            $scope.locales = ['en', 'ru'];
        });

    // Array to contain selected properties (yes - we only can select one, but ng-grid isn't smart enough)
    $scope.selectedMessages = [];

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
        data: 'messages',
        enableRowReordering: true,
        headerRowHeight: 28,
        multiSelect: false,
        keepLastSelected: false,
        selectedItems: $scope.selectedMessages,
        columnDefs: [{field: 'key', displayName: 'Key'}]
    }

        // Click handler for add button
    $scope.addMessage = function() {
        var value = {};
        for (var i = 0; i < $scope.locales.length; i++) {
            value[$scope.locales[i]] = '';
        }
        $scope.messages.push({
            key : '',
            value: value});
    };

    // Click handler for remove button
    $scope.removeMessage = function() {
        if ($scope.selectedMessages.length > 0) {
            var index = $scope.messages.indexOf($scope.selectedMessages[0]);
            $scope.gridOptions.selectItem(index, false);
            $scope.messages.splice(index, 1);

            $scope.selectedMessages.length = 0;
            if (index < $scope.messages.length) {
                $scope.gridOptions.selectItem(index + 1, true);
            } else if ($scope.messages.length > 0) {
                $scope.gridOptions.selectItem(index - 1, true);
            }
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

        if ($scope.messages.length > 0) {
            $scope.property.value = {};
            $scope.property.value = $scope.messages;
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