function Search($scope, $http) {
    $http.get('latin.json').success(function (data) {
        $scope.Words = data;
    });
}

Search.$inject = ['$scope', '$http'];
angular.module('app', ['angular.filter']).controller('Search', Search);
