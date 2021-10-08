var express = require('express');
var router = express.Router();
var User = require('../models/user');
var passport = require('passport');

// render landing page
router.get('/', (req, res) => {
    res.render('landing');
});

// render register page
router.get('/register', (req, res) => {
    res.render('register');
});

// submit register form, and save to MongoDB
router.post('/register', (req, res) => {
    var newUser = new User({username: req.body.username});
    User.register(newUser, req.body.password, (err, user) => {
        if (err) {
            req.flash('error', err.message);
            return res.render('register');
        }
        passport.authenticate('local')(req, res, () => {
            req.flash('success', 'Welcome to YelpCamp, ' + user.username + '!');
            res.redirect('/campgrounds');
        });
    });
});

// render login page
router.get('/login', (req, res) => {
    res.render('login');
});

// submit login form
router.post('/login', passport.authenticate('local', 
    {
        successRedirect: '/campgrounds',
        failureRedirect: '/login'
    }), (req, res) => {
});

// logout
router.get('/logout', (req, res) => {
    req.logout();
    res.redirect('/campgrounds');
});

module.exports = router;
