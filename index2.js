function Search($scope, $http) {
    $http.get('latin.json').success(function (data) {
        $scope.Words = data;
    });
}

Search.$inject = ['$scope'];
angular.module('app', []).controller('Search', Search);
