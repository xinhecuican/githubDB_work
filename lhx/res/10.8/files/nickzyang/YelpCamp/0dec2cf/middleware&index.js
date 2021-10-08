var Campground = require('../models/campground');
var Comment = require('../models/comment');

var middlewareObject = {};

// check ownership of a certain campground
middlewareObject.checkCampgroundOwnership = function checkCampgroundOwnership(req, res, next) {
    if (req.isAuthenticated()) {
        Campground.findById(req.params.id, (err, foundCampground) => {
            if (err) {
                req.flash('error', 'Server is busy, please retry.');
                res.redirect('back');
            } else {
                if (foundCampground.author.id.equals(req.user._id)) {
                    next();
                } else {
                    req.flash('error', 'You don\'t have permission to do that.');
                    res.redirect('back');
                }
            }
        });
    } else {
        req.flash('error', 'You need to be logged in to do that.');
        res.redirect('back');
    }
};

// check ownership of a certain comment
middlewareObject.checkCommentOwnership = function checkCommentOwnership(req, res, next) {
    if (req.isAuthenticated()) {
        Comment.findById(req.params.comment_id, (err, foundComment) => {
            if (err) {
                req.flash('error', 'Server is busy, please retry.');
                res.redirect('back');
            } else {
                if (foundComment.author.id.equals(req.user._id)) {
                    next();
                } else {
                    req.flash('error', 'You don\'t have permission to do that.');
                    res.redirect('back');
                }
            }
        });
    } else {
        req.flash('error', 'You need to be logged in to do that.');
        res.redirect('back');
    }
};

// check login status
middlewareObject.isLoggedIn = function isLoggedIn(req, res, next) {
    if (req.isAuthenticated()) {
        return next();
    }
    req.flash('error', 'You need to be logged in to do that.');
    res.redirect('/login');
};

module.exports = middlewareObject;
