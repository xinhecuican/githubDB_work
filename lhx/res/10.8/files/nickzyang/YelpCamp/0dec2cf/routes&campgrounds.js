var express = require('express');
var router = express.Router();
var Campground = require('../models/campground');
var middleware = require('../middleware');

// read all campgrounds from MongoDB and render
router.get('/', (req, res) => {
    Campground.find({}, (err, campgrounds) => {
        if (err) {
            console.log(err);
        } else {
            res.render("campgrounds/index", {campgrounds: campgrounds});
        }
    });
});

// add new campground (requiring logged in)
router.get('/new', middleware.isLoggedIn, (req, res) => {
    res.render('campgrounds/new');
});

// RESTful routes, post new campgrounds
router.post('/', middleware.isLoggedIn, (req, res) => {
    var campName = req.body.campName;
    var campPrice = req.body.campPrice;
    var campImg = req.body.campImg;
    var campDescription = req.body.campDescription;
    var author = {
        id: req.user._id,
        username: req.user.username
    }
    var newCampground = {
        name: campName,
        price: campPrice,
        img: campImg,
        description: campDescription,
        author: author
    };
    Campground.create(newCampground, (err, camp) => {
        if (err) {
            console.log(err);
        } else {
            res.redirect('/campgrounds');
        }
    });
});

// certain campground page
router.get('/:id', (req, res) => {
    Campground.findById(req.params.id).populate('comments').exec((err, camp) => {
        if (err) {
            console.log(err);
        } else {
            res.render('campgrounds/show', { campground: camp });
        }
    });
});

// render edit page
router.get('/:id/edit', middleware.checkCampgroundOwnership, (req, res) => {
    Campground.findById(req.params.id, (err, foundCampground) => {
        if (err) {
            res.redirect('back');
        }
        res.render('campgrounds/edit', { campground: foundCampground });
    });
});

// submit campground changes
router.put('/:id', middleware.checkCampgroundOwnership, (req, res) => {
    Campground.findOneAndUpdate({ _id: req.params.id }, req.body.campground, (err, updatedCamp) => {
        if (err) {
            res.redirect('/campgrounds');
        } else {
            res.redirect('/campgrounds/' + req.params.id);
        }
    });
});

// delete campground, requiring the same user that created it
router.delete('/:id', middleware.checkCampgroundOwnership, (req, res) => {
    Campground.findOneAndRemove({ _id: req.params.id }, (err) => {
        if (err) {
            res.redirect('/campgrounds');
        } else {
            res.redirect('/campgrounds');
        }
    });
});

module.exports = router;
