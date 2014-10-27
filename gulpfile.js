(function() {

    var gulp   = require('gulp'),
        jshint = require('gulp-jshint');

    gulp.task('build', function gulpBuild(){
        gulp.src(['common/common.css', 'common/common.js'])
            .pipe(gulp.dest('example/vendor/recipes'))
    });

    gulp.task('hint', function gulpHint() {
        return gulp.src(['common/common.js'])
            .pipe(jshint('.jshintrc'))
            .pipe(jshint.reporter('default'));
    });

    gulp.task('test', ['hint']);
    gulp.task('default', ['test', 'build']);

})();