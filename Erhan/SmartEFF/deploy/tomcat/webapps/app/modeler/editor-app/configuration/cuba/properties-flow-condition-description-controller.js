var KisBpmFlowConditionDescriptionCtrl = [ '$scope', '$modal', '$timeout', '$translate', function($scope, $modal) {

    // Config for the modal window
    var opts = {
        template:  'editor-app/configuration/properties/cuba/flow-condition-description-popup.html?version=' + Date.now(),
        scope: $scope
    };

    // Open the dialog
    $modal(opts);
}];


var KisBpmFlowConditionDescriptionPopupCtrl = ['$scope', function($scope) {

    // Put json representing flow condition description on scope
    if ($scope.property.value !== undefined && $scope.property.value !== null && $scope.property.value !== "") {

        if ($scope.property.value.constructor == String) {
            $scope.description = JSON.parse($scope.property.value);
        } else {
            // Note that we clone the json object rather then setting it directly,
            // this to cope with the fact that the user can click the cancel button and no changes should have happended
            $scope.description = angular.copy($scope.property.value);
        }
    } else {
        $scope.description = {outcome: "", operation: ">", count: "0"};
    }

    // we can build a condition expression only for flow node that is located after gateway that in
    // its turn located after userTask. We try to find the task and extract its id and outcomes.
    // Id and outcome name are necessary for building a condition expression. If task is not found then
    // no control is visible on the form.
    if ($scope.selectedShape.incoming[0] != undefined && $scope.selectedShape.incoming[0].incoming[0] != undefined) {
        var prevTask = $scope.selectedShape.incoming[0].incoming[0].incoming[0];
        if (prevTask != undefined) {
            $scope.formVisible = true;
            $scope.description.prevTaskId = prevTask.properties['oryx-overrideid'];
            $scope.description.taskResourceId = prevTask.resourceId;
            var taskOutcomes = prevTask.properties['oryx-taskoutcomes'];
            if (taskOutcomes != undefined) {
                $scope.outcomes = taskOutcomes;
            } else {
                $scope.formVisible = false;
            }
        } else {
            $scope.formVisible = false;
        }
    }

    // Click handler for save button
    $scope.save = function() {
        $scope.property.value = $scope.description
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