var KisBpmSubModelCtrl = [ '$scope', '$http', function ($scope, $http) {

    fillModels($scope, $http);

    // Put json representing flow condition description on scope
    if ($scope.property.value !== undefined && $scope.property.value !== null && $scope.property.value !== "") {
        if ($scope.property.value.constructor == String) {
            $scope.submodel = JSON.parse($scope.property.value);
        } else {
            // Note that we clone the json object rather then setting it directly,
            // this to cope with the fact that the user can click the cancel button and no changes should have happended
            $scope.submodel = angular.copy($scope.property.value);
        }
    } else {
        $scope.submodel = {actModelId: ""};
    }

    $scope.updateProperty = function() {
        $scope.property.value = $scope.submodel;
        $scope.updatePropertyInModel($scope.property);
    }
}];

var KisBpmSubModelDisplayCtrl = [ '$scope', '$http', function ($scope, $http) {

    $scope.setCurrentModelName = function () {
        for (var i = 0; i < $scope.models.length; i++) {
            var model = $scope.models[i];
            if (model.actModelId === $scope.property.value.actModelId) {
                $scope.modelName = model.name;
                break;
            }
        }
    }

    if ($scope.property.value !== undefined && $scope.property.value !== null && $scope.property.value !== "") {
        if ($scope.editor.models !== undefined) {
            $scope.models = $scope.editor.models;
            $scope.setCurrentModelName();
        } else {
            fillModels($scope, $http);
            $scope.$watch('models', function (newValue, oldValue) {
                if (newValue !== undefined) {
                    $scope.setCurrentModelName();
                }
            });
        }
    }
}];


function fillModels($scope, $http) {
    if ($scope.editor.models !== undefined) {
        $scope.models = $scope.editor.models;
    } else {
        $http.get(KISBPM.URL.getAllModels())
            .success(function (data) {
                $scope.editor.models = data;
                $scope.models = data;
            });
    }
}