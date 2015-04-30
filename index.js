function Search($scope, $http) {
    $http.get('./latin.json').success(function (data) {
        $scope.Words = data;
    });
}
