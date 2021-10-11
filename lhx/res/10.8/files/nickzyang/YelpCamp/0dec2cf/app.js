var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var Campground = require('./models/campground');
var Comment = require('./models/comment');
var User = require('./models/user');
var seedDB = require('./seeds');
var path = require('path');
var passport = require('passport');
var LocalStrategy = require('passport-local');
var session = require('express-session');
var campgroundRoutes = require('./routes/campgrounds');
var commentRoutes = require('./routes/comments');
var indexRoutes = require('./routes/index');
var methodOverride = require('method-override');
var flash = require('connect-flash');

mongoose.connect('mongodb://localhost:27017/test', {useNewUrlParser: true, useUnifiedTopology: true});

var app = express();

app.use(bodyParser.urlencoded( {extended: true} ));
app.use(express.static(path.join(__dirname, '/public')));
app.set('view engine', 'ejs');
app.use(methodOverride('_method'));
app.use(flash());

app.use(session({
    secret: 'Red is the best album by TS!',
    resave: false,
    saveUninitialized: false
}));

app.use(passport.initialize());
app.use(passport.session());
passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

app.use((req, res, next) => {
    res.locals.currentUser = req.user;
    res.locals.error = req.flash('error');
    res.locals.success = req.flash('success');
    next();
});

app.use('/', indexRoutes);
app.use('/campgrounds', campgroundRoutes);
app.use('/campgrounds/:id/comments', commentRoutes);

app.listen(3000, () => {
    console.log('Express is running...');
});
