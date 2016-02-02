var app = angular.module('app',['ngRoute']);
 
app.config(function($routeProvider){
 
   	$routeProvider
 
   	.when('/cadastro', {
   		title: 'Cadastro',
      	templateUrl : 'app/views/user/register.html',
      	controller  : 'RegisterCtrl',
   	})
 
   	// caso não seja nenhum desses, redirecione para a rota '/'
   	.otherwise ({ redirectTo: '/' });
});