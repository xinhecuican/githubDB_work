var express = require('express');
var router = express.Router({ mergeParams: true });
var Campground = require('../models/campground');
var Comment = require('../models/comment');
var middleware = require('../middleware');

// create new comment, requiring logged in
router.get('/new', middleware.isLoggedIn, (req, res) => {
    Campground.findById(req.params.id, (err, camp) => {
        if (err) {
            console.log(err);
        } else {
            res.render('comments/new', {campground: camp});
        }
    });
});

// submit new comment
router.post('/', middleware.isLoggedIn, (req, res) => {
    Campground.findById(req.params.id, (err, camp) => {
        if (err) {
            req.flash('error', 'Server is busy, please retry.');
            res.redirect('back');
        } else {
            Comment.create(req.body.comment, (err, comment) => {
                if (err) {
                    console.log(err);
                } else {
                    comment.author.id = req.user._id;
                    comment.author.username = req.user.username;
                    comment.save();
                    camp.comments.push(comment);
                    camp.save();
                    req.flash('success', 'Successfully added comment!');
                    res.redirect('/campgrounds/' + camp._id);
                }
            });
        }
    });
});

// render comment edit page
router.get('/:comment_id/edit', middleware.checkCommentOwnership, (req, res) => {
    Comment.findById(req.params.comment_id, (err, foundComment) => {
        if (err) {
            res.redirect('back');
        } else {
            res.render('comments/edit', { campground_id: req.params.id, comment: foundComment });
        }
    });
});

// submit comment changes
router.put('/:comment_id', middleware.checkCommentOwnership, (req, res) => {
    Comment.findByIdAndUpdate({ _id: req.params.comment_id }, req.body.comment, (err, updatedComment) => {
        if (err) {
            res.redirect('back');
        } else {
            res.redirect('/campgrounds/' + req.params.id);
        }
    });
});

// delete certain comment, requiring the same user that created it
router.delete('/:comment_id', middleware.checkCommentOwnership, (req, res) => {
    Comment.findOneAndRemove({ _id: req.params.comment_id }, (err) => {
        if (err) {
            res.redirect('back');
        } else {
            req.flash('success', 'Comment deleted.');
            res.redirect('/campgrounds/' + req.params.id);
        }
    });
});

module.exports = router;
