var KisBpmFlowOutcomeCtrl = [ '$scope', function ($scope) {

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
        $scope.description = {outcome: "", taskResourceId: ""};
    }

    //find previous task outcomes
    if ($scope.selectedShape.incoming[0] != undefined && $scope.selectedShape.incoming[0].incoming[0] != undefined) {
        var prevTask = $scope.selectedShape.incoming[0].incoming[0].incoming[0];
        if (prevTask != undefined) {
            $scope.description.taskResourceId = prevTask.resourceId;
            var taskOutcomes = prevTask.properties['oryx-taskoutcomes'];
            if (taskOutcomes != undefined) {
                $scope.outcomes = taskOutcomes;
            }
        }
    }

    $scope.updateProperty = function() {
        $scope.property.value = $scope.description;
        $scope.updatePropertyInModel($scope.property);
    }
}];