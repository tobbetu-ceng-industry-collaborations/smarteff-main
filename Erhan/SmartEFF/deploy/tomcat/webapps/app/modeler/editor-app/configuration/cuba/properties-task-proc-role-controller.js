var KisBpmTaskProcRoleCtrl = [ '$scope', function ($scope) {

    var procRoles = $scope.editor.getCanvas().properties['oryx-procroles'];
    if (procRoles != undefined && procRoles != null && procRoles != "") {
        //For some reason procRoles collection may be stringified twice
        //todo gorbunkov to figure out why it happens
        if (typeof procRoles === "string") {
            procRoles = JSON.parse(procRoles);
            if (typeof procRoles === "string") {
                procRoles = JSON.parse(procRoles);
            }
        }
    } else {
        procRoles = [];
    }
    $scope.procRoles = procRoles;

    $scope.updateProperty = function() {
        $scope.updatePropertyInModel($scope.property);
    }
}];