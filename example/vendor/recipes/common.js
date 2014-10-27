(function($window, $jquery, $q) {

    "use strict";

    /**
     * @module Recipes
     * @link https://github.com/Wildhoney/Recipes
     * @version $id$
     */
    $window.RecipesInterface = function RecipesInterface() {};

    /**
     * @property prototype
     * @type {Object}
     */
    $window.RecipesInterface.prototype = {

        /**
         * @constant API_URL
         * @type {String}
         */
        API_URL: 'http://recipes-learn-app.herokuapp.com/',

        /**
         * @method makeRequest
         * @param path {String}
         * @param [type='GET'] {String}
         * @param [params={}] {Object}
         * @return {Q.promise}
         */
        makeRequest: function makeRequest(path, type, params) {

            var deferred = $q.defer();

            $jquery.ajax({
                url: this.APP_URL + path,
                data: params || {},
                dataType: 'json',
                type: type || 'GET',
                success: function success(response) {

                deferred.resolve(response);

            }.bind(this)});

            return deferred.promise;
            
        },

        /**
         * @method addRecipe
         * @param name {String}
         * @param description {String}
         * @param ingredients {Array}
         * @return {Q.promise}
         */
        addRecipe: function addRecipe(name, description, ingredients) {

            return this.makeRequest('recipes', 'POST', {
                name:        name,
                description: description,
                ingredients: ingredients
            });

        },

        /**
         * @method deleteRecipe
         * @param recipeModel {Object}
         * @return {Q.promise}
         */
        deleteRecipe: function deleteRecipe(recipeModel) {
            return this.makeRequest('recipes/' + recipeModel._id, 'DELETE');
        },

        /**
         * @method getRecipes
         * @return {Q.promise}
         */
        getRecipes: function getRecipes() {
            return this.makeRequest('recipes', 'GET');
        }

    };

})(window, window.jQuery, window.Q);